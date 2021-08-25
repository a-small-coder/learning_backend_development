from rest_framework import serializers

from ...models import Ball, Treadmill, TennisTable, SubImage, Category, SubCategory
from ..main.serializers import CategoryForProductSerializer, SubCategorySerializer


class ProductListSerializer(serializers.Serializer):

    category = serializers.SerializerMethodField()
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    slug = serializers.SlugField()
    main_image = serializers.ImageField()
    short_description = serializers.CharField()
    price = serializers.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        fields = ['category', 'id', 'title', 'slug', 'main_image', 'short_description', 'price']

    @staticmethod
    def get_category(obj):
        return CategoryForProductSerializer(Category.objects.get(id=obj.category_id)).data


class AbstractRetrieveSerializer(serializers.Serializer):

    category = serializers.SerializerMethodField()
    sub_images = serializers.SerializerMethodField()

    @staticmethod
    def get_sub_images(obj):
        return SubImageSerializer(obj.sub_images.all(), many=True).data

    @staticmethod
    def get_category(obj):
        return CategoryForProductSerializer(Category.objects.get(id=obj.category_id)).data


class BallRetrieveSerializer(serializers.ModelSerializer, AbstractRetrieveSerializer):

    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = Ball
        fields = '__all__'

    @staticmethod
    def get_subcategory(obj):
        return SubCategorySerializer(SubCategory.objects.get(id=obj.subcategory_id)).data


class TreadmillRetrieveSerializer(serializers.ModelSerializer, AbstractRetrieveSerializer):

    class Meta:
        model = Treadmill
        fields = '__all__'


class TennisTableRetrieveSerializer(serializers.ModelSerializer, AbstractRetrieveSerializer):

    class Meta:
        model = TennisTable
        fields = '__all__'


class SubImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubImage
        fields = ['image']


