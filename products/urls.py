from django.urls import path
from .views import(
    ProductListView,ProductdetailView,
    CategoryListView,CategorydetailView,
    FileListView,FiledetailView
)


urlpatterns = [
    
    path('products/',ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/',ProductdetailView.as_view(), name='product-detail'),

    path('categories/',CategoryListView.as_view(),name='category-list'),
    path('categories/<int:pk>/',CategorydetailView.as_view(),name='category-detail'),

    path('products/<int:product_id>/files/',FileListView.as_view(),name='file-list'),
    path('products/<int:product_id>/files/<int:pk>/',FiledetailView.as_view(),name='file-detali')
]
 