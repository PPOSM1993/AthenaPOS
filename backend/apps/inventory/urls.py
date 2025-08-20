from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryMovementViewSet

router = DefaultRouter()
router.register(r"inventory", InventoryMovementViewSet, basename="inventory")

urlpatterns = [
    path("", include(router.urls)),
]
