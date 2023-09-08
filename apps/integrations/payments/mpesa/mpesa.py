from rest_framework import generics, serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.payments.models import MpesaTransaction
from apps.products.models import Product

from .mpesa_callback_data import mpesa_callback_data_distructure
from .utils import MpesaGateWay


class LipaNaMpesaSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    #amount = serializers.IntegerField(default=0)
    product = serializers.IntegerField()


class LipaNaMpesaCallbackSerializer(serializers.Serializer):
    body = serializers.JSONField(required=False)


class LipaNaMpesaCallbackAPIView(generics.CreateAPIView):
    serializer_class = LipaNaMpesaCallbackSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        product_id = request.query_params.get("product")
        print(f"Mpesa Data: {data}")
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid(raise_exception=True):

            product = Product.objects.filter(id=product_id).first()

            if product:
                product.promotion_budget_paid = True
                product.save()

            callback_data = mpesa_callback_data_distructure(data)
            mpesa_transaction = MpesaTransaction.objects.create(**callback_data)
            mpesa_transaction.product_id = product_id
            mpesa_transaction.save()

            print(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LipaNaMpesaAPIView(generics.CreateAPIView):
    serializer_class = LipaNaMpesaSerializer

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):  
            product_id = serializer.validated_data.get("product")
            product = Product.objects.get(id=product_id)

            amount = product.promotion_budget

            mpesa = MpesaGateWay()
            mpesa.stk_push(
                phone_number=data.get('phone_number'),
                amount=int(amount),
                callback_url=f"https://df3c-105-163-1-68.ngrok-free.app/integrations/lipa-na-mpesa-callback/?product={product_id}",
                account_reference="Influencer Marketing API",
                transaction_desc="This is wallet topup mpesa transaction"
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
