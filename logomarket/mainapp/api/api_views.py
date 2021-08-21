from rest_framework.viewsets import ModelViewSet

from .serializers import CategorySerializer, CartListSerializer, CartRetrieveSerializer
from ..models import Category, Cart


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class CartViewSet(ModelViewSet):

    queryset = Cart.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CartRetrieveSerializer
        else:
            return CartListSerializer
