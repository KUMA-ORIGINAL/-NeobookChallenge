from rest_framework import serializers

from market.models import Category, Product, Order, Cart


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


# class OrderItemSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = OrderItem
#         fields = ('quantity', 'product')


class CartSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context['request'].user
        product = validated_data['product']
        quantity = validated_data['quantity']
        cart, created = Cart.objects.get_or_create(user=user, product=product, defaults={'quantity': quantity})
        if not created:
            cart.quantity += quantity
            cart.save()
        return cart


class OrderSerializer(serializers.ModelSerializer):
    products = CartSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'phone_number', 'address', 'reference_point', 'comment', 'products')
        # fields = '__all__'

    def create(self, validated_data):
        products_data = validated_data.pop('products', [])  # Получаем данные о продуктах
        order = Order.objects.create(**validated_data)  # Создаем заказ
        for product_data in products_data:
            order.products.add(product_data)
        return order
