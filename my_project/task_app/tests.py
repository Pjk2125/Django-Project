from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import YourModel

class YourModelAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.your_model = YourModel.objects.create(name='Test Model')

    def test_get_your_model(self):
        url = reverse('your-model-detail', kwargs={'pk': self.your_model.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
