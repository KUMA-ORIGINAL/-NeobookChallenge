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
        fields = ('quantity', 'product')


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'phone_number', 'address', 'reference_point', 'comment', 'products')
