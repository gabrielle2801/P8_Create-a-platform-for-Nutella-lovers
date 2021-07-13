# from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.urls import reverse_lazy

from product.views import ProductListView
from product.models import Product


class ProductListTest(TestCase):
    def setUp(self):
        # self.url = reverse_lazy('Muesli')
        self.list_url = reverse_lazy('product_list', kwargs={
            'search_product': 'Muesli'})

    def test_get_queryset(self):
        request = RequestFactory().get('/product_list')
        view = ProductListView()
        view.request = request

        qs = view.get_queryset()

        self.assertQuerysetEqual(qs, Product.objects.all())

    def test_status_code_302(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.list_url +
                             f"?search_product={'Muesli'}",)
