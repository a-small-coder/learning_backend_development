from rest_framework.viewsets import ModelViewSet

from .serializers import CategorySerializer, CartSerializer
from ..models import Category, Cart, Product, Ball


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class CartViewSet(ModelViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'slug'
