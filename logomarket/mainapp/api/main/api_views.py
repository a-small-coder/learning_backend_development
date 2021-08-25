from rest_framework.viewsets import ModelViewSet

from .serializers import *


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'