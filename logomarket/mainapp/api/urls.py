from django.urls import path
from rest_framework import routers

from .api_views import CategoryViewSet

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')

urlpatterns = []
urlpatterns += router.urls
