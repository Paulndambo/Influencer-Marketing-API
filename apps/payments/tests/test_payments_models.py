from decimal import Decimal

from django.test import TestCase

from apps.payments.models import PaymentRecord, Wallet
from apps.products.models import Product
from apps.users.models import Customer, Influencer, User


class WalletTestCase(TestCase):
    def setUp(self) -> None:
        self.customer_user = User.objects.create(
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

        self.influencer_user = User.objects.create(
            username="testinfluencer",
            password="testpassword",
            role="influencer",
            email="influencer@gmail.com"
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
        
        return super().setUp()
    
    def test_create_wallet(self):
        wallet = Wallet.objects.create(
            user=self.influencer_user, 
            withdrawn=0,
            balance=0
        )

        self.assertEqual(str(wallet), self.influencer_user.email)

    def test_wallet_balance_is_decimal(self):
        wallet = Wallet.objects.create(
            user=self.influencer_user, 
            withdrawn=0,
            balance=0.0
        )
        self.assertTrue(isinstance(wallet.balance, Decimal) or isinstance(wallet.balance, float))