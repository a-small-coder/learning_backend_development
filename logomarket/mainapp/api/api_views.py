from rest_framework.viewsets import ModelViewSet

from .serializers import *
from ..models import Category, Cart, Ball, Treadmill, TennisTable


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


class BallViewSet(ModelViewSet):

    queryset = Ball.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            pass
            # return BallRetrieveSerializer
        else:
            return ProductListSerializer


class TreadmillViewSet(ModelViewSet):

    queryset = Treadmill.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            pass
            # return TreadmillRetrieveSerializer
        else:
            return ProductListSerializer


class TennisTableViewSet(ModelViewSet):

    queryset = TennisTable.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            pass
            # return TennisTableRetrieveSerializer
        else:
            return ProductListSerializer
