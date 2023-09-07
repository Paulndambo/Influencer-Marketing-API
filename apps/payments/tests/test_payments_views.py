from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from apps.payments.models import PaymentRecord, Wallet
from apps.products.models import Product
from apps.users.models import Customer, Influencer, User

wallets_url = reverse("wallets-list")
payments_url = reverse("payments-list")


class WalletsAndPaymentsViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.customer_user = User.objects.create_user(
            username="testcustomer",
            password="testpassword",
            role="customer",
            email="customer@gmail.com"
        )

        self.customer = Customer.objects.create(
            user=self.customer_user,
            phone_number="0745491093",
            address="228-90119, Matuu-Kenya"
        )

        self.user = User.objects.create_user(
            username="testinfluencer",
            password="testpassword",
            role="influencer",
            email="influencer@gmail.com"
        )
        self.influencer_user = User.objects.create(
            username="testinfluencer1",
            password="testpassword",
            role="influencer",
            email="influencer1@gmail.com"
        )

        self.influencer = Influencer.objects.create(
            user=self.influencer_user,
            phone_number="0745491093",
            address="228-90119",
            city="Nairobi",
            country="Kenya"
        )

        self.product = Product.objects.create(
            name="Test Product",
            price=35000.0,
            promotion_budget=500,
            customer=self.customer
        )

        #self.token = Token.objects.create(user=self.user)

        self.client.login(username="testinfluencer", password="testpassword")

        # return super().setUp()

    def test_get_wallets_list(self):
        res = self.client.get(wallets_url)
        self.assertEqual(res.status_code, 200)

    def test_create_wallet(self):
        self.influencer_user.refresh_from_db()
        payload = {
            "user": self.influencer_user.id,
            "balance": 500.00,
            "withdrawn": 50.00
        }
        res = self.client.post(wallets_url, payload)
        self.assertEqual(res.status_code, 201)

    def test_wallet_update(self):
        self.influencer_user.refresh_from_db()

        wallet = Wallet.objects.create(
            user=self.influencer_user,
            withdrawn=0,
            balance=200.0
        )

        updated_payload = {
            "user": self.influencer_user.id,
            "withdrawn": 80,
            "balance": 120
        }
        res = self.client.put(
            f"/payments/wallets/{wallet.id}/", updated_payload, format="json")
        self.assertEqual(res.status_code, 200)

    def test_get_payment_records(self):
        res = self.client.get("/payments/payments/")
        self.assertEqual(res.status_code, 200)

    def test_create_payment_record(self):
        self.product.refresh_from_db()
        self.influencer.refresh_from_db()

        payload = {
            "influencer": self.influencer.id,
            "product": self.product.id,
            "amount": 5000.0
        }
        res = self.client.post("/payments/payments/", payload)
        self.assertEqual(res.status_code, 201)

    def test_payment_record_update(self):
        self.product.refresh_from_db()
        self.influencer.refresh_from_db()

        payment = PaymentRecord.objects.create(
            influencer=self.influencer,
            product=self.product,
            amount=2500.0
        )

        updated_payload = {
            "influencer": self.influencer.id,
            "product": self.product.id,
            "amount": 3500.0
        }
        res = self.client.put(
            f"/payments/payments/{payment.id}/", updated_payload, format="json")
        self.assertEqual(res.status_code, 200)
