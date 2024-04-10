from django.urls import path
from django.views.decorators.cache import cache_page

from marketApp.utils import published, unpublished
from marketApp.views import main, ProductCreateView, ProductUpdateView, ProductListView, ProductDetailView, \
    ProductDeleteView, CategoryCreateView, CategoryUpdateView, CategoryListView, CategoryDeleteView
from marketApp.apps import MarketappConfig

app_name = MarketappConfig.name
urlpatterns = [

    path('', main, name='main'),

    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/list', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/detail', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),

    path('product/<int:pk>/published', published, name='product_published'),
    path('product/<int:pk>/unpublished', unpublished, name='product_unpublished'),

    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update', CategoryUpdateView.as_view(), name='category_update'),
    path('category/list', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/delete', CategoryDeleteView.as_view(), name='category_delete'),

]
