from django.test import TestCase

from apps.users.models import (Influencer, InfluencerPreference,
                               InfluencerProfilePhoto, InfluencerProfileVideo,
                               InfluencerWorkExperience, SocialProfile, User)


class InfluencerBaseTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="influencer", role="influencer", email="influencer@gmail.com", password="influencer"
        )
        self.influencer = Influencer.objects.create(
            user=self.user,
            phone_number="0745491093",
            address="228-90119",
            city="Nairobi",
            country="Kenya"
        )
        return super().setUp()


class InfluencerTestCase(InfluencerBaseTestCase):
    def test_influencer_is_created(self):
        self.assertEqual(self.influencer.user.email, "influencer@gmail.com")
        self.assertTrue(isinstance(self.influencer.user, User))
        self.assertTrue(isinstance(self.influencer, Influencer))

    def test_influencer_stringified(self):
        self.assertEqual(str(self.influencer), self.user.username)


class InfluencerWorkExprienceTestCase(InfluencerBaseTestCase):
    def test_create_work_experience(self):
        experience = InfluencerWorkExperience.objects.create(
            influencer=self.influencer,
            title="Software Engineer",
            employer="Ryanada Limited",
            job_type="full-time",
            work_environment="onsite",
            start_date="2023-08-22",
            description="Building applications using python"
        )

        self.assertEqual(str(experience), "Software Engineer")
        self.assertTrue(isinstance(experience, InfluencerWorkExperience))
        self.assertTrue(isinstance(experience.title, str))

    def test_create_multiple_work_experiences(self):
        experiences = [
            {
                "influencer": self.influencer,
                "title": "Software Engineer",
                "employer": "Ryanada Limited",
                "job_type": "full-time",
                "work_environment": "onsite",
                "start_date": "2023-08-22",
                "description": "Building applications using python"
            },
            {
                "influencer": self.influencer,
                "title": "Software Engineer",
                "employer": "Click2Sure Holdings Limited",
                "job_type": "full-time",
                "work_environment": "onsite",
                "start_date": "2022-03-07",
                "end_date": "2023-08-01",
                "description": "Building applications using Python & Django"
            }
        ]

        experiences_list = []

        for x in experiences:
            experiences_list.append(
                InfluencerWorkExperience(
                    influencer=x["influencer"],
                    title=x["title"],
                    employer=x["employer"],
                    job_type=x["job_type"],
                    work_environment=x["work_environment"],
                    start_date=x["start_date"],
                    end_date=x.get("end_date"),
                    description=x["description"]
                )   
            )
        InfluencerWorkExperience.objects.bulk_create(experiences_list)

        self.assertEqual(InfluencerWorkExperience.objects.count(), 2)


class InfluencerSocialProfilesTestCase(InfluencerBaseTestCase):
    def test_social_profiles_create(self):
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

        self.assertEqual(str(profiles), self.influencer.user.username)


class InfluencerPreferencesTestCase(InfluencerBaseTestCase):
    def test_preference_create(self):
        preference = InfluencerPreference.objects.create(
            influencer=self.influencer,
            preferred_platforms=["twitter", "facebook", "tiktok"],
            min_targetted_age=10,
            max_targetted_age=100,
            preferred_brand_types=["cars", "electronics", "watches"]
        )

        self.assertEqual(str(preference), self.user.email)

    def test_preference_data_types(self):
        preference = InfluencerPreference.objects.create(
            influencer=self.influencer,
            preferred_platforms=["twitter", "facebook", "tiktok"],
            min_targetted_age=10,
            max_targetted_age=100,
            preferred_brand_types=["cars", "electronics", "watches"]
        )
        self.assertTrue(preference.preferred_platforms, list)

    def test_preference_empty_fields(self):
        preference = InfluencerPreference.objects.create(
            influencer=self.influencer,
            preferred_platforms=[],
            min_targetted_age=10,
            max_targetted_age=100,
            preferred_brand_types=[]
        )
        self.assertEqual(preference.preferred_platforms, [])

class InfluencerProfileVideoTestCase(InfluencerBaseTestCase):
    def test_profile_video_create(self):
        profile_video = InfluencerProfileVideo.objects.create(
            influencer=self.influencer,
            video=f"https://www.example.com/profile-videos/{self.influencer.id}/"
        )
        self.assertEqual(str(profile_video), self.user.username)

    def test_video_link_can_be_empty(self):
        profile_video = InfluencerProfileVideo.objects.create(
            influencer=self.influencer
        )
        self.assertIsNone(profile_video.video, "Profile video link is empty")