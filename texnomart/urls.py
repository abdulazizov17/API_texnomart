from django.urls import path, include
from rest_framework.routers import DefaultRouter

from texnomart.views import category, product, comment, attribute


urlpatterns = [
    path('categories/', category.CategoryListApiView.as_view(), name='category-list'),
    path('category/<int:pk>/', category.CategoryDetailApiView.as_view(), name='category-detail'),
    path('categories/<slug:category_slug>/', category.CategoryDetailApiView.as_view(), name='category-detail'),
    path('products/', product.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', product.ProductDetailView.as_view(), name='product_detail'),
    path('product/', product.ProductCreateListView.as_view(), name='product-create'),
    path('product/<int:pk>/edit/', product.ProductEditView.as_view(), name='product-edit'),
    path('product/<int:pk>/delete/', product.ProductDeleteView.as_view(), name='product-delete'),
    path('all-images/', product.ImageListApiView.as_view(), name='all-products'),
    path('all-comment/', comment.CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('all-comments/', comment.CommentDetailAPIView.as_view(), name='comment-detail'),



]

