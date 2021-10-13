from django.test import TestCase, Client
from accounts.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestAccounts(TestCase):

    def setUp(self, pk):
        self.client = Client()
        user = get_object_or_404(User, pk=pk)
