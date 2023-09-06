from decimal import Decimal

from django.test import TestCase

from apps.products.models import Product


class ProductTestCase(TestCase):

    def setUp(self) -> None:
        self.product = Product.objects.create(
            name="Test Product",
            price=180000.0,
            product_url="https://example.com/products/",
            promotion_budget=4500.0
        )
        return super().setUp()


    def test_product_name_str(self):
        self.assertEqual(str(self.product), self.product.name)

        
    def test_product_count(self):
        products_count = Product.objects.count()
        self.assertEqual(products_count, 1)

    def test_product_name_update(self):
        self.product.name = "Test Product Updated"
        self.product.save()
        self.assertEqual(self.product.name, "Test Product Updated")

    def test_product_price_is_decimal(self):
        self.assertTrue(isinstance(self.product.price, Decimal) or isinstance(self.product.price, float))