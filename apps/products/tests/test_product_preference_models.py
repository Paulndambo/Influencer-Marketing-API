from decimal import Decimal

from django.test import TestCase

from apps.products.models import Product, ProductCampaignPreference


class ProductCampaignTestCase(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(
            name="Test Product",
            price=180000.0,
            product_url="https://example.com/products/",
            promotion_budget=4500.0
        )

        return super().setUp()

    def test_product_preference_create(self):
        product_preference = ProductCampaignPreference.objects.create(
            product=self.product,
            min_targetted_age=1,
            max_targetted_age=89,
            target_platforms=["instagram", "twitter", "snapchat"],
            min_followers_on_target_platform=1000,
            min_engagement_percentage=10
        )

        self.assertEqual(str(product_preference), self.product.name)
        self.assertListEqual(product_preference.target_platforms, ["instagram", "twitter", "snapchat"])
        self.assertTrue(isinstance(product_preference.target_platforms, list))
    