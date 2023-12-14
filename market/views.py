from django.shortcuts import render
from rest_framework import generics

from market.models import Category
from market.serializers import CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
