from rest_framework import serializers

from market.models import Category, Product, OrderItem, Order


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'photo')


class ProductFullSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    # def create(self, validated_data):
    #     products_data = validated_data.pop('products')
    #     order = Order.objects.create(**validated_data)
    #     for product_data in products_data:
    #         OrderItem.objects.create(order=order, **product_data)
    #     return {
    #         'id': order.id,
    #         'created': order.created
    #     }
