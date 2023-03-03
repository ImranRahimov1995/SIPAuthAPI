from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class LatencyAPIViewTest(APITestCase):
    def test_get_latency(self):
        url = reverse('latency')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('latency', response.data)
        self.assertTrue(response.data['latency'].endswith('ms'))

