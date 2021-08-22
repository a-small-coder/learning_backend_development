from django.urls import path
from rest_framework import routers

from .api_views import CategoryViewSet, CartViewSet, BallViewSet, TreadmillViewSet, TennisTableViewSet

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('cart', CartViewSet, basename='cart')
router.register('ball', BallViewSet, basename='ball')
router.register('treadmill', TreadmillViewSet, basename='treadmill')
router.register('tennistable', TennisTableViewSet, basename='tennistable')

urlpatterns = []
urlpatterns += router.urls
