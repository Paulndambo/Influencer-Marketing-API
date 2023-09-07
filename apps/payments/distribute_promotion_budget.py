from decimal import Decimal

from apps.payments.models import PaymentRecord, Wallet
from apps.products.models import Product


def distribute_promotion_budget(product: Product):
    """

    Takes in a product
    - Checks if the product campaign limit has been reached and influencers not paid.
    - Distributes the product promotion budget to all influencers wallets who promoted it based on engagement %

    Parameters:
    - product: an object

    Returns:
    - None

    """
    campaigns = product.productcampaigns.all()

    if not campaigns:
        return

    for campaign in campaigns:
        influencer = campaign.influencer
        # Calculate payment based on engagement metrics and product budget.
        total_campaign_engagement = 0
        total_product_engagement = 0
        if campaign.clicks > 0:
            total_campaign_engagement = Decimal(campaign.clicks)
            total_product_engagement = Decimal(sum(product.productcampaigns.values_list("clicks", flat=True)))

        payment_amount = 0
        if total_campaign_engagement > 0:
            engagement_percentage = total_campaign_engagement / total_product_engagement
            payment_amount = Decimal(product.promotion_budget) * Decimal(engagement_percentage)

        # Distribute the payment to the influencer's wallet.
        wallet = Wallet.objects.filter(user=influencer.user).first()
        if not wallet:
            wallet = Wallet.objects.create(user=influencer.user, balance=0, withdrawn=0)

        wallet.balance += payment_amount
        wallet.save()

        # Record the payment in PaymentRecord model.
        payment_record = PaymentRecord.objects.create(
            influencer=influencer,
            product=product,
            amount=payment_amount
        )
        payment_record.save()

        campaign.influencer_paid = True
        campaign.save()