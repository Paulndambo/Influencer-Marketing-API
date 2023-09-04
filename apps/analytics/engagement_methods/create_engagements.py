from apps.analytics.models import Engagement, PromotionCampaign


def create_engagement(
    existing_engagement: Engagement,
    current_campaign: PromotionCampaign,
    product: int,
    influencer: int,
    device_id: str,
    ip_address: str,
    country: str,
    city: str
):
    # Catch fraudulent engagement
    if existing_engagement:
        engagement = Engagement.objects.create(
            product_id=product,
            influencer_id=influencer,
            device_id=device_id,
            customer_ip=ip_address,
            likes=0,
            views=0,
            comments=0,
            clicks=0,
            status="fraudulent",
            country=country,
            city=city
        )
    else:
        engagement = Engagement.objects.create(
            product_id=product,
            influencer_id=influencer,
            device_id=device_id,
            customer_ip=ip_address,
            likes=0,
            comments=0,
            status="clean",
            country=country,
            city=city
        )
        engagement.record_views_and_clicks()
        if current_campaign:
            current_campaign.record_engagement()
