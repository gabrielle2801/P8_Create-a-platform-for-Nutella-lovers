from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product


def product(request):
    if 'search_product' in request.GET and request.GET['search_product']:
        search_product = request.GET['search_product']
        products = Product.objects.filter(name__startswith=search_product)
        return render(request, 'product.html',
                      {'products': products, 'query': search_product})
    else:
        return HttpResponse('Please ...')
