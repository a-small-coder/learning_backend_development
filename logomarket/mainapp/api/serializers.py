from rest_framework import serializers

from ..models import *


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


class CartListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class CartRetrieveSerializer(serializers.ModelSerializer):

    cart_products = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'owner', 'total_products', 'total_price', 'for_anonymous_user', 'cart_products']

    @staticmethod
    def get_cart_products(obj):
        return CartProductSerializer(CartProduct.objects.filter(cart=obj), many=True).data


class CartProductSerializer(serializers.ModelSerializer):

    item = serializers.SerializerMethodField()

    class Meta:
        model = CartProduct
        fields = ['item', 'qty', 'total_price']

    @staticmethod
    def get_item(obj):
        return ProductListSerializer(obj.content_type.model_class().objects.get(id=obj.object_id)).data


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
        return CategoryForProductListSerializer(Category.objects.get(id=obj.category_id)).data


class CategoryForProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BallRetrieveSerializer(serializers.ModelSerializer):

    sub_images = serializers.SerializerMethodField()

    class Meta:
        model = Ball
        fields = '__all__'

    @staticmethod
    def get_sub_images(obj):
        return SubImageSerializer(obj.sub_images.all(), many=True).data


class TreadmillRetrieveSerializer(serializers.ModelSerializer):

    sub_images = serializers.SerializerMethodField()

    class Meta:
        model = Treadmill
        fields = '__all__'

    @staticmethod
    def get_sub_images(obj):
        return SubImageSerializer(obj.sub_images.all(), many=True).data


class TennisTableRetrieveSerializer(serializers.ModelSerializer):

    sub_images = serializers.SerializerMethodField()

    class Meta:
        model = Treadmill
        fields = '__all__'

    @staticmethod
    def get_sub_images(obj):
        return SubImageSerializer(obj.sub_images.all(), many=True).data


class SubImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubImage
        fields = ['image']
