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
        # fields = '__all__'

    def create(self, validated_data):
        products_data = validated_data.pop('products', [])  # Получаем данные о продуктах
        order = Order.objects.create(**validated_data)  # Создаем заказ

        # Для каждого продукта создаем OrderItem и связываем его с заказом
        for product_data in products_data:
            # Получаем данные о продукте
            product_id = product_data.get('product')
            quantity = product_data.get('quantity')
            # Получаем экземпляр Product по его ID
            product = Product.objects.get(pk=product_id)

            # Создаем OrderItem для данного заказа и продукта
            order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity)
        return order