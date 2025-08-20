from django.urls import path
from .views import SalesReportView, StockReportView, SupplierReportView

urlpatterns = [
    path("sales/", SalesReportView.as_view(), name="sales-report"),
    path("stock/", StockReportView.as_view(), name="stock-report"),
    path("suppliers/", SupplierReportView.as_view(), name="suppliers-report"),
]
