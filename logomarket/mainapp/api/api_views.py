from rest_framework.generics import ListAPIView

from .serializers import CategorySerializer
from ..models import Category, SubCategory


class CategoryListAPIView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
