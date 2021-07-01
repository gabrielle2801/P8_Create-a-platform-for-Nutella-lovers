from django.urls import path

from product.views import ProductListView

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product'),
]
