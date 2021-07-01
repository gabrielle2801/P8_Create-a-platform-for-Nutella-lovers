from django.shortcuts import render
# from django.views import View

from product.models import Product


def product_detail(request, form):
    products = Product.objects.all()
    print(form)
    return render(request, 'product.html', {'product': products})
