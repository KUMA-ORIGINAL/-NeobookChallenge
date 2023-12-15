from django.shortcuts import render
from rest_framework import generics

from market.models import Category, Product
from market.serializers import CategorySerializer, ProductSerializer, ProductFullSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
