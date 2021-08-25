from django.urls import path
from rest_framework import routers

from .main.api_views import CategoryViewSet
from .cart.api_views import CartViewSet
from .product.api_views import BallViewSet, TreadmillViewSet, TennisTableViewSet


router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('cart', CartViewSet, basename='cart')
router.register('balls', BallViewSet, basename='balls')
router.register('treadmills', TreadmillViewSet, basename='treadmills')
router.register('tennis_tables', TennisTableViewSet, basename='tennis_tables')

urlpatterns = []
urlpatterns += router.urls
