
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from apps.users.models import Influencer


# Create your views here.
class ProductViewSet(ModelViewSet):
    """
    Description:
    - This view is reponsible for;-
        - fetching products and returning to the user.
        - creating, edit, and deleting products.

    Parameters:
    - None

    Returns:
    - json_data: Response data based on the current user
        - if not logged in, the user will see all posted products.
        - if user is customer, they will see all the products they have posted.
        - if user is influencer, they will see all products which they have not promoted yet.
        - if user is admin, will see all the products.

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == "customer":
                return self.queryset.filter(customer__user=user)
            elif user.role == "influencer":
                influencer = Influencer.objects.get(user=user)
                influencer_promos = list(
                    influencer.campaigns.values_list("product", flat=True)
                )
                return self.queryset.exclude(id__in=influencer_promos)
        return self.queryset
