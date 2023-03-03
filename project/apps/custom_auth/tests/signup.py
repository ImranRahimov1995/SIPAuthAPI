from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.custom_auth.models import ExpiringToken
from apps.users.models import CustomUser


class SignUpViewTest(APITestCase):
    url = reverse('signup')

    def test_signup_valid_data(self):
        data = {
            'email': 'testuser@example.com',
            'username': 'testuser',
            'password': 'password',
            'phone': '+994702215209'
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        token_key = response.data['token']
        token = ExpiringToken.objects.get(key=token_key)
        user = CustomUser.objects.get(email=data['email'])

        self.assertEqual(token.user, user)

    def test_signup_invalid_data(self):

        data = {
            'email': 'testuser@example.com',
            'username': 'testuser',
            'password': 'password',
            'phone': '+99470215209'
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertIn('phone', response.data)
