from django.test import TestCase
from ecommerceapp.models import *


class EcommerceAppTestCase(TestCase):

      def setUp(self):
            self.data = Category.objects.create(name="elder", slug="elder")
            self.user = User.objects.create(username="admin")
      
      def test_category_model(self):
            data1 = self.data
            self.assertTrue(isinstance(data1, Category))