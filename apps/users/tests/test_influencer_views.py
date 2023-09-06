
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.users.models import Influencer, SocialProfile, User, InfluencerWorkExperience

influencers_url = reverse("influencers-list")


def load_influencer(user):
    influencer = Influencer.objects.create(
        user=user,
        phone_number="0745491093",
        address="228-90119",
        city="Nairobi",
        country="Kenya"
    )
    return influencer


class TestInfluencerViewBase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="influencer", role="influencer", email="influencer@gmail.com", password="influencer"
        )
        self.influencer_user = User.objects.create_user(
            username="influencer2", role="influencer", email="influencer2@gmail.com", password="influencer"
        )
        self.influencer = load_influencer(self.influencer_user)
        self.client.login(username="influencer", password="influencer")
        return super().setUp()


class TestInfluencerView(TestInfluencerViewBase):
    def test_get_influencer_list(self):
        res = self.client.get(influencers_url)
        self.assertEqual(res.status_code, 200)

    def test_influencer_create(self):
        payload = {
            "user": self.user.id,
            "phone_number": "0745491093",
            "address": "228-90119",
            "city": "Nairobi",
            "country": "Kenya"
        }

        res = self.client.post(influencers_url, payload)
        self.assertEqual(res.status_code, 201)

    def test_update_influencer(self):
        self.influencer.refresh_from_db()

        updated_payload = {
            "user": self.influencer.user.id,
            "phone_number": "0745491093",
            "address": "228-90119",
            "city": "Nairobi",
            "country": "Kenya"
        }

        update_url = f"/users/influencers/{self.influencer.id}/"
        res = self.client.put(update_url, updated_payload,
                              content_type="application/json", format="json")
        self.assertEqual(res.status_code, 200)

    def test_delete_influencer(self):
        delete_url = f"/users/influencers/{self.influencer.id}/"
        res = self.client.delete(delete_url)
        self.assertEqual(res.status_code, 204)


class InfluencerComponentsBaseTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="influencer", role="influencer", email="influencer@gmail.com", password="influencer"
        )
        self.influencer = load_influencer(self.user)
        self.client.login(username="influencer", password="influencer")
        return super().setUp()


class TestInfluencerSocialProfileView(InfluencerComponentsBaseTestCase):

    def test_get_social_profiles_list(self):
        self.influencer.refresh_from_db()

        res = self.client.get(f"/users/influencers/{self.influencer.id}/social-profiles/")
        self.assertEqual(res.status_code, 200)

    def test_social_profile_create(self):
        self.influencer.refresh_from_db()

        payload = {
            "influencer": self.influencer.id,
            "instagram": f"https://instgram.com/@{self.user.username}",
            "facebook": f"https://facebook.com/@{self.user.username}",
            "twitter": f"https://twitter.com/@{self.user.username}",
            "tiktok": f"https://tiktok.com/@{self.user.username}",
            "threads": f"https://threads.com/@{self.user.username}",
            "youtube": f"https://youtube.com/@{self.user.username}",
            "telegram": f"https://telegram.com/@{self.user.username}",
            "snapchat": f"https://snapchar.com/@{self.user.username}",
            "whatsapp_number": self.influencer.phone_number,
        }

        res = self.client.post(f"/users/influencers/{self.influencer.id}/social-profiles/", payload)
        self.assertEqual(res.status_code, 201)

    def test_delete_social_profile(self):
        self.influencer.refresh_from_db()

        profiles = SocialProfile.objects.create(
            influencer=self.influencer,
            instagram=f"https://instgram.com/@{self.user.username}",
            facebook=f"https://facebook.com/@{self.user.username}",
            twitter=f"https://twitter.com/@{self.user.username}",
            tiktok=f"https://tiktok.com/@{self.user.username}",
            threads=f"https://threads.com/@{self.user.username}",
            youtube=f"https://youtube.com/@{self.user.username}",
            telegram=f"https://telegram.com/@{self.user.username}",
            snapchat=f"https://snapchar.com/@{self.user.username}",
            whatsapp_number=self.influencer.phone_number,
        )

        res = self.client.delete(
            f"/users/influencers/{self.influencer.id}/social-profiles/{profiles.id}/")
        self.assertEqual(res.status_code, 204)


class TestInfluencerWorkExperienceView(InfluencerComponentsBaseTestCase):
    def test_get_experiences_list(self):
        self.influencer.refresh_from_db()

        res = self.client.get(f"/users/influencers/{self.influencer.id}/work-experiences/")
        self.assertEqual(res.status_code, 200)

    
    def test_work_experience_create(self):
        self.influencer.refresh_from_db()
        payload = {
            "influencer": self.influencer.id,
            "title": "Software Engineer",
            "employer":"Ryanada Limited",
            "job_type": "full-time",
            "work_environment": "onsite",
            "start_date": "2023-08-22",
            "description": "Building applications using python"
        }

        res = self.client.post(f"/users/influencers/{self.influencer.id}/work-experiences/", payload)
        self.assertEqual(res.status_code, 201)

    def test_work_experience_update(self):
        self.influencer.refresh_from_db()

        experience = InfluencerWorkExperience.objects.create(
            influencer=self.influencer,
            title="Software Engineer",
            employer="Ryanada Limited",
            job_type="full-time",
            work_environment="onsite",
            start_date="2023-08-22",
            description="Building applications using python"
        )

        updated_payload = {
            "influencer": self.influencer.id,
            "title": "Software Engineer",
            "employer": "Click2Sure Holdings Limited",
            "job_type": "full-time",
            "work_environment": "onsite",
            "start_date": "2022-03-07",
            "end_date": "2023-08-01",
            "description": "Building applications using Python & Django"
        }
        res = self.client.put(f"/users/influencers/{self.influencer.id}/work-experiences/{experience.id}/", updated_payload, content_type="application/json", format="json")
        self.assertEqual(res.status_code, 200)

    def test_work_experience_delete(self):
        experience = InfluencerWorkExperience.objects.create(
            influencer=self.influencer,
            title="Software Engineer",
            employer="Ryanada Limited",
            job_type="full-time",
            work_environment="onsite",
            start_date="2023-08-22",
            description="Building applications using python"
        )
        res = self.client.delete(f"/users/influencers/{self.influencer.id}/work-experiences/{experience.id}/")
        self.assertEqual(res.status_code, 204)
