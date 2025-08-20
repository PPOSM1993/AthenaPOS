from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PublisherViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'publishers', PublisherViewSet, basename='publisher')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
