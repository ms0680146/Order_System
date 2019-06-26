from django.test import TestCase, Client
from django.urls import reverse
from orders.models import Order, OrderItem
from datetime import datetime
from django.utils.timezone import get_current_timezone
import pytz

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_home_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'layout.html')

    def test_piechart_GET(self):
        response = self.client.get(reverse('piechart'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/piechart.html')

    def test_cohort_GET(self):
        response = self.client.get(reverse('cohort'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/cohort.html')

    def test_barchart_GET(self):
        response = self.client.get(reverse('barchart'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/barchart.html')

    def test_get_shipping_data_GET(self):
        tz = get_current_timezone()
        shipping_free = Order.objects.create(
            order_id=1,
            customer_id=10,
            shipping=0,
            created_at=tz.localize(datetime.now())
        )
        shipping_need = Order.objects.create(
            order_id=2,
            customer_id=14,
            shipping=80,
            created_at=tz.localize(datetime.now())
        )
        response = self.client.get(reverse('api-shipping-data'))
        self.assertJSONEqual(response.content, {"labels": ["free shipping", "need shipping"], "counts": [1, 1]})
    
    def test_get_top3_products_GET(self):
        product1 = OrderItem.objects.create(
            order_id=1,
            product_name='product1',
            qty=3
        )
        product2 = OrderItem.objects.create(
            order_id=2,
            product_name='product2',
            qty=2
        )
        product2_1 = OrderItem.objects.create(
            order_id=3,
            product_name='product2',
            qty=5
        )
        product3 = OrderItem.objects.create(
            order_id=4,
            product_name='product3',
            qty=1
        )
        product4 = OrderItem.objects.create(
            order_id=5,
            product_name='product4',
            qty=2
        )
        response = self.client.get(reverse('api-top3-products'))
        self.assertJSONEqual(response.content, {"labels": ["product2", "product1", "product4"],  "counts": [7, 3, 2]})