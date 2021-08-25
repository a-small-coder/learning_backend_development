from rest_framework import serializers

from ..product.serializers import ProductListSerializer
from ...models import Cart, CartProduct


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
