from rest_framework import serializers

from ..models import Category, SubCategory, Cart, CartProduct


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

    class Meta:
        model = CartProduct
        fields = ['content_type', 'object_id', 'qty', 'total_price']


class Product(serializers.ModelSerializer):

    pass


