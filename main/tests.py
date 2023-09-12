from django.test import TestCase, Client
from .models import Product
from django.utils import timezone

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_products_url_is_exist(self):
        response = Client().get('/main/products/')
        self.assertEqual(response.status_code, 200)

    def test_main_products_using_products_template(self):
        response = Client().get('/main/products/')
        self.assertTemplateUsed(response, 'products.html')

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name="Chitato", amount=100, price=10000, date_added=timezone.now, description="Chips")

    def test_string_method(self):
        product = Product.objects.get(id=1)
        expected_string = f"Name: {product.name} {product.amount} {product.price} {product.date_added} {product.description}"
        self.assertEqual(str(product), expected_string)