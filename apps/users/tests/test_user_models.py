from django.test import TestCase

from apps.users.models import User


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.customer_user = User.objects.create_user(
            username="customer", role="customer", email="customer@gmail.com", password="customer"
        )
        self.influencer_user = User.objects.create_user(
            username="influencer", role="influencer", email="influencer@gmail.com", password="influencer"
        )

        self.admin_user = User.objects.create_user(
            username="admin", role="admin", email="admin@gmail.com", password="admin"
        )

        return super().setUp()

    def test_customer_user_role(self):
        self.assertEqual(self.customer_user.role, "customer")

    def test_influencer_user_role(self):
        self.assertEqual(self.influencer_user.role, "influencer")
    
    def test_admin_user_role(self):
        self.assertEqual(self.admin_user.role, "admin")
