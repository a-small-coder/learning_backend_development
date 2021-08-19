from django.urls import path
from rest_framework import routers

from .api_views import CategoryViewSet, CartViewSet

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('cart', CartViewSet, basename='cart')

urlpatterns = []
urlpatterns += router.urls
