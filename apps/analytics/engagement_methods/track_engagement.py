from apps.analytics.models import Engagement

class ViewsAndClicksProcessor:
    def __init__(self, influencer, product):
        self.influencer = influencer
        self.product = product

    def record_views_and_clicks(self):
        try:
            engagement = Engagement.objects.get(
                influencer=self.influencer, 
                product=self.product
            )

            engagement.clicks += 1
            engagement.views += 1
            engagement.save()

        except Engagement.DoesNotExist:
            pass



class CommentsAndLikesProcessor:
    def __init__(self, influencer, product):
        self.influencer = influencer
        self.product = product

    def record_comments(self):
        pass

    def record_likes(self):
        pass
