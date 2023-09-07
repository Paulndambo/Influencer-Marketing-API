from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.users.models import User

users_url = reverse("users-list")
login_url = reverse("login")
register_url = reverse("register")


class TestUserView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="admin", email="admin@gmail.com", password="admin", role="admin", is_superuser=True
        )
        
        self.client.login(username="admin", password="admin")
        return super().setUp()

    def test_get_users(self):
        res = self.client.get(users_url)
        print(f"Super User Check: {self.user.is_superuser}")
        self.assertEqual(res.status_code, 200)

    def test_user_login(self):
        payload = {
            "username": "admin",
            "password": "admin"
        }
        res = self.client.post(login_url, payload)
        response_content = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(response_content['role'], "admin")

    def test_user_reqister(self):
        payload = {
            "username": "testuser",
            "email": "testuser@gmail.com",
            "password": "testuser",
            "role": "customer"
        }
        res = self.client.post(register_url, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
