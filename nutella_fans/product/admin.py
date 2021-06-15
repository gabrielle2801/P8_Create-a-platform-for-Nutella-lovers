from django.contrib import admin
from .models import Product, Category, Brand, Store

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Store)
