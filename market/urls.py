from django.urls import path

from market import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category-list'),
    path('product/', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:id>', views.ProductRetrieveView.as_view(), name='product-detail')
]
