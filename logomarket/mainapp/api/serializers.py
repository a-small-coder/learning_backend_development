from rest_framework import serializers

from ..models import Category, SubCategory


# class SubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    #subcategories = SubCategorySerializer(many=True, read_only=True)

    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
