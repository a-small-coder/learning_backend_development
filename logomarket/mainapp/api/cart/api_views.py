from rest_framework.viewsets import ModelViewSet

from .serializers import *


class CartViewSet(ModelViewSet):

    queryset = Cart.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CartRetrieveSerializer
        else:
            return CartListSerializer