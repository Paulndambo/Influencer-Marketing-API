from decimal import Decimal

from django.test import TestCase

from apps.payments.models import PaymentRecord, Wallet
from apps.products.models import Product
from apps.users.models import Customer, Influencer, User


class WalletAndPaymentRecordTestCase(TestCase):
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

        self.wallet = Wallet.objects.create(
            user=self.influencer_user,
            withdrawn=0,
            balance=0.0
        )

        return super().setUp()

    def test_create_wallet(self):
        self.assertEqual(str(self.wallet), str(1))

    def test_wallet_balance_is_decimal(self):
        self.assertTrue(isinstance(self.wallet.balance, Decimal)
                        or isinstance(self.wallet.balance, float))

    def test_wallet_recharge(self):
        self.wallet.balance += 56000.0
        self.wallet.save()
        self.assertGreater(self.wallet.balance, 0)

    def test_create_payment_record(self):
        payment = PaymentRecord.objects.create(
            influencer=self.influencer,
            product=self.product,
            amount=2500.0
        )

        self.assertEqual(str(payment), str(payment.id))

    def test_payment_creation_updates(self):
        payment = PaymentRecord.objects.create(
            influencer=self.influencer,
            product=self.product,
            amount=2500.0
        )
        self.wallet.balance += payment.amount
        self.wallet.save()

        self.assertEqual(self.wallet.balance, 2500.0)
