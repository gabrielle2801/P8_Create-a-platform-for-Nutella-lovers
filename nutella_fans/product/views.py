from django.views.generic import ListView

from product.models import Product


class ProductListView(ListView):
    template_name = 'product_list.html'
    model = Product

    def get_queryset(self):
        search = self.request.GET.get('search_product', '').strip()
        qs = super().get_queryset()
        if search:

            return qs.filter(name__icontains=search).order_by(
                'nutriscore').distinct()
        else:
            return qs
