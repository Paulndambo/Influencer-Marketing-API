import django

django.setup()

import json

import pytest
from django.test import Client, TestCase
from django.urls import reverse

from apps.products.models import Product
from apps.users.models import Customer, Influencer, User
        