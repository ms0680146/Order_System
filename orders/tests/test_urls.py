from django.test import SimpleTestCase
from django.urls import reverse, resolve
from orders.views import home, piechart, cohort, barchart, get_shipping_data, get_top3_products

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_piechart_url_resolves(self):
        url = reverse('piechart')
        self.assertEquals(resolve(url).func, piechart)

    def test_cohort_url_resolves(self):
        url = reverse('cohort')
        self.assertEquals(resolve(url).func, cohort)
    
    def test_barchart_url_resolves(self):
        url = reverse('barchart')
        self.assertEquals(resolve(url).func, barchart)

    def test_get_shipping_data_url_resolves(self):
        url = reverse('api-shipping-data')
        self.assertEquals(resolve(url).func, get_shipping_data)
    
    def test_get_top3_products_url_resolves(self):
        url = reverse('api-top3-products')
        self.assertEquals(resolve(url).func, get_top3_products)