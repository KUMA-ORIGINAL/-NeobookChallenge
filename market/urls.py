from django.urls import path

from market import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category-list')
]
