from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaleViewSet, SaleSearchView

router = DefaultRouter()
router.register(r"sales", SaleViewSet, basename="sales")

urlpatterns = [
    path("", include(router.urls)),
    path("sales/search/", SaleSearchView.as_view(), name="sale-search"),
]
