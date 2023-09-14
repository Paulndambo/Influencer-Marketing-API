from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.products.models import Product, ProductCampaignPreference
from apps.users.models import Customer, User


class TestProductPreferenceView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="customer", 
            role="customer", 
            email="customer@gmail.com", 
            password="customer"
        )
        self.customer = Customer.objects.create(
            user=self.user,
            phone_number="0746740960",
            address="228-90119, Nairobi - Kenya"
        )
        self.product = Product.objects.create(
            name="Test Product",
            price=180000.0,
            product_url="https://example.com/products/",
            promotion_budget=4500.0,
            customer=self.customer
        )

        self.client.login(username="customer", password="customer")
        return super().setUp()

    
    def test_get_preferences_list(self):
        res = self.client.get(f"/products/{self.product.id}/preferences/")
        self.assertEqual(res.status_code, 200)

    def test_product_preference_create(self):
        self.product.refresh_from_db()

        payload = {
            "product": self.product.id,
            "min_targetted_age":1,
            "max_targetted_age": 89,
            "target_platforms":'["instagram", "twitter", "snapchat"]',
            "min_followers_on_target_platform": 1000,
            "min_engagement_percentage": 10
        }
        res = self.client.post(f"/products/{self.product.id}/preferences/", payload)
        self.assertEqual(res.status_code, 201)


    def test_product_preference_update(self):
        self.product.refresh_from_db()

        product_preference = ProductCampaignPreference.objects.create(
            product=self.product,
            min_targetted_age=1,
            max_targetted_age=89,
            target_platforms=["instagram", "twitter", "snapchat"],
            min_followers_on_target_platform=1000,
            min_engagement_percentage=10
        )

        updated_payload = {
            "product": self.product.id,
            "min_targetted_age":1,
            "max_targetted_age": 120,
            "target_platforms":'["instagram", "twitter", "snapchat", "tiktok", "facebook"]',
            "min_followers_on_target_platform": 12500,
            "min_engagement_percentage": 23
        }

        res =self.client.put(f"/products/{self.product.id}/preferences/{product_preference.id}/", updated_payload, format="json")
        self.assertEqual(res.status_code, 200)

    def test_product_preference_delete(self):
        self.product.refresh_from_db()

        product_preference = ProductCampaignPreference.objects.create(
            product=self.product,
            min_targetted_age=1,
            max_targetted_age=89,
            target_platforms=["instagram", "twitter", "snapchat"],
            min_followers_on_target_platform=1000,
            min_engagement_percentage=10
        )

        res =self.client.delete(f"/products/{self.product.id}/preferences/{product_preference.id}/")
        self.assertEqual(res.status_code, 204)


    
