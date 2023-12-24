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

    def perform_create(self, serializer):
        products = self.request.data.get('products')
        order = serializer.save(user=self.request.user)
        for product in products:
            order_item = OrderItem.objects.create(order=order, **product)
            order.products.add(order_item)


class UserOrderListView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
