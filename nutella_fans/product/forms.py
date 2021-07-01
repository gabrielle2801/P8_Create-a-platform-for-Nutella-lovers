from django.forms import forms, ModelForm

from product.models import Brand, Product, Category, Store


class ProductForm(ModelForm):
    class Meta:
        model = Product
