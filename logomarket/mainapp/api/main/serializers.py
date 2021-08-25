from rest_framework import serializers

from ...models import Category, SubCategory


class CategoryForProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'subcategories']

    @staticmethod
    def get_subcategories(obj):
        return SubCategorySerializer(SubCategory.objects.filter(category=obj), many=True).data


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug']



