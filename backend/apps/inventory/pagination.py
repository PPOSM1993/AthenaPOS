# utils/pagination.py
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    """
    Paginación estándar para todas las vistas del proyecto.
    - page_size: número de resultados por defecto
    - page_size_query_param: permite al cliente cambiar el tamaño de página (?page_size=20)
    - max_page_size: límite máximo para no sobrecargar el servidor
    """
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        """
        Personalizamos la respuesta para entregar más claridad
        """
        return Response({
            "count": self.page.paginator.count,   # total de registros
            "total_pages": self.page.paginator.num_pages,  # total de páginas
            "current_page": self.page.number,     # página actual
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data
        })
