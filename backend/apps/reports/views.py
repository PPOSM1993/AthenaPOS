from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count, F
from django.utils.dateparse import parse_date
from apps.sales.models import Sale, SaleItem
from apps.products.models import Product
from apps.inventory.models import InventoryMovement
from apps.suppliers.models import Supplier
from .serializers import DateRangeSerializer
from rest_framework import status

class SalesReportView(APIView):
    """
    Reporte de ventas totales y productos más vendidos
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = DateRangeSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        start_date = serializer.validated_data["start_date"]
        end_date = serializer.validated_data["end_date"]

        # Ventas totales
        sales = Sale.objects.filter(date__range=[start_date, end_date], status="completed")
        total_sales = sales.aggregate(total_amount=Sum("total"))["total_amount"] or 0
        total_items_sold = SaleItem.objects.filter(sale__in=sales).aggregate(total_quantity=Sum("quantity"))["total_quantity"] or 0

        # Productos más vendidos
        top_products = (
            SaleItem.objects.filter(sale__in=sales)
            .values("product__name")
            .annotate(total_sold=Sum("quantity"))
            .order_by("-total_sold")[:10]
        )

        return Response({
            "total_sales_amount": total_sales,
            "total_items_sold": total_items_sold,
            "top_products": list(top_products)
        }, status=status.HTTP_200_OK)


class StockReportView(APIView):
    """
    Reporte de stock crítico (productos con stock menor o igual a un límite)
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        limit = int(request.query_params.get("limit", 5))
        critical_stock = Product.objects.filter(stock__lte=limit).order_by("stock")
        data = [{"product": p.name, "stock": p.stock} for p in critical_stock]
        return Response({"critical_stock": data}, status=status.HTTP_200_OK)


class SupplierReportView(APIView):
    """
    Reporte de proveedores más activos según cantidad de productos vendidos
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = DateRangeSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        start_date = serializer.validated_data["start_date"]
        end_date = serializer.validated_data["end_date"]

        # Contar cantidad de productos vendidos por proveedor
        suppliers_activity = (
            SaleItem.objects.filter(
                sale__date__range=[start_date, end_date],
                sale__status="completed",
                product__publisher__isnull=False
            )
            .values("product__publisher__name")
            .annotate(total_sold=Sum("quantity"))
            .order_by("-total_sold")[:10]
        )

        return Response({"top_suppliers": list(suppliers_activity)}, status=status.HTTP_200_OK)
