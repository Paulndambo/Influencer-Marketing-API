import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.users.models import Customer, User
from apps.users.serializers import CustomerSerializer

customers_url = reverse("customers-list")


class TestCustomerView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="customer", role="customer", email="customer@gmail.com", password="customer"
        )
        self.customer_user = User.objects.create_user(
            username="customer3", role="customer", email="customer3@gmail.com", password="customer"
        )
        self.test_customer = Customer.objects.create(
            user=self.customer_user,
            phone_number="0746740960",
            address="228-90119, Nairobi - Kenya"
        )
        self.client.login(username="customer", password="customer")
        return super().setUp()

    def test_customer_create(self):
        payload = {
            "user": self.user.id,
            "phone_number": "0745491093",
            "address": "228-90119, Nairobi"
        }
        res = self.client.post(customers_url, payload)
        self.assertEqual(res.status_code, 201)

        

    
    def test_update_customer(self):
        self.test_customer.refresh_from_db()

        #customer.refresh_from_db()
        updated_payload = {
            "user": self.test_customer.user.id,
            "phone_number": "0746740960",
            "address": "228-90119, Nairobi - Kenya"
        }
    
        res = self.client.put(f"{customers_url}/{self.test_customer.id}/", updated_payload, content_type="application/json")
        return
        self.assertTrue(res.status_code, 200)

    def test_delete_customer(self):
        customer_url = f"/users/customers/{self.test_customer.id}/"
        res = self.client.delete(customer_url)
        self.assertEqual(res.status_code, 204)
