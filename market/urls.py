from django.urls import path

from market import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category-list'),
    path('product/', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>', views.ProductRetrieveView.as_view(), name='product-detail'),
    path('order/', views.OrderCreateView.as_view(), name='order-create'),
    path('user-orders/', views.UserOrderListView.as_view(), name='user-order-list'),
]
