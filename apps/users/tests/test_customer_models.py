from django.test import TestCase

from apps.users.models import Customer, User


class CustomerTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="customer", role="customer", email="customer@gmail.com", password="customer"
        )
        return super().setUp()

    def test_customer_create(self):
        customer = Customer.objects.create(
            user=self.user,
            phone_number="0745491093",
            address="228-90119, Nairobi"
        )

        self.assertEqual(customer.user.email, "customer@gmail.com")
        self.assertTrue(isinstance(customer.user, User))
        self.assertTrue(isinstance(customer, Customer))

    def test_customer_stringified(self):
        customer = Customer.objects.create(
            user=self.user,
            phone_number="0745491093",
            address="228-90119, Nairobi"
        )
        self.assertEqual(str(customer), self.user.username)