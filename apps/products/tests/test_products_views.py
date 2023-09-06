from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from apps.users.models import Customer, User

products_url = reverse("products-list")


class TestProductView(TestCase):
    def setUp(self) -> None:

        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword', role="customer")
        self.customer = Customer.objects.create(user=self.user, phone_number="0745491093", address="228-90119, Matuu, Kenya")

        self.payload = {
            "name": "Test Product",
            "price": 180000.0,
            "promotion_budget": 4500,
            "customer": self.customer
        }
        self.product = Product.objects.create(**self.payload)

        self.client.login(username="testuser", password="testpassword")

        return super().setUp()

    def test_get_products_list(self):
        res = self.client.get(products_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_product(self):

        payload = {
            "name": "Test Product 3",
            "price": 4590.0,
            "promotion_budget": 30
        }

        res = self.client.post(products_url, payload)
        self.assertEqual(res.status_code, 201)

    def test_product_update(self):
        self.product.refresh_from_db()

        updated_payload = {
            "name": "Test Product II Updated",
            "price": 180000.0,
            "promotion_budget": 4500,
            "customer": self.customer.id
        }
        serializer = ProductSerializer(data=updated_payload)
        serializer.is_valid(raise_exception=True)
        serialized_data = serializer.data

        product_patch_url = f"/products/{self.product.id}/"

        res = self.client.put(
            product_patch_url, serialized_data, format='json')
        self.assertEqual(res.status_code, 200)

    def test_product_delete(self):
        product_delete_url = f"/products/{self.product.id}/"
        res = self.client.delete(product_delete_url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
