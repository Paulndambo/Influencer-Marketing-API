from rest_framework import generics, serializers, status
from rest_framework.response import Response

from apps.payments.models import Wallet
from apps.users.models import User


class ProcessCustomerManualPayment(object):
    def __init__(self, email, amount):
        self.email = email
        self.amount = amount

    def process_customer_manual_payment(self):
        print(f"Email: {self.email}, Amount: {self.amount}")
        try:
            user = User.objects.filter(email=self.email).first()

            # The user must be a customer not an influencer
            if not user.role == "customer":
                pass

            wallet = Wallet.objects.filter(user=user).first()

            # If customer does not have a wallet, create it for them
            if not wallet:
                wallet = Wallet.objects.create(
                    user=user,
                    withdrawn=0,
                    balance=self.amount
                )

            # Update balance of existing wallet
            else:
                wallet.balance += self.amount
                wallet.save()
        except Exception as e:
            raise e

class ManualPaymentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)


class ManualPaymentAPIView(generics.CreateAPIView):
    serializer_class = ManualPaymentSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            amount = serializer.validated_data.get("amount")
            try:
                manual_payment = ProcessCustomerManualPayment(email, amount)
                manual_payment.process_customer_manual_payment()

            except Exception as e:
                raise e
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)