from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from market.models import Category, Product, Order, OrderItem
from market.serializers import CategorySerializer, ProductSerializer, ProductFullSerializer, OrderSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        # Получаем данные о продуктах из запроса
        products_data = self.request.data.get('products', [])

        # Создаем заказ и связанные с ним OrderItem в цикле для каждого продукта
        order = serializer.save(user=self.request.user)  # Сохраняем заказ и привязываем к пользователю

        for product_data in products_data:
            product_id = product_data.get('id')  # Получаем ID продукта из данных запроса
            quantity = product_data.get('quantity', 1)  # Получаем количество продукта

            # Получаем экземпляр Product по его ID
            product = Product.objects.get(pk=product_id)

            # Создаем OrderItem для данного заказа и продукта
            order_item = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )
            order.products.add(product)


class UserOrderListView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
