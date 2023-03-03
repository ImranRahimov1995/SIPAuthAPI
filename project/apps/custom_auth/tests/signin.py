from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.custom_auth.models import ExpiringToken
from apps.users.models import CustomUser


class SignInViewTest(APITestCase):
    url = reverse('signin')

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='CustomUser',
            email='testuser@example.com',
            password='password'
        )

    def test_signin_valid_credentials(self):
        data = {
            'username': 'CustomUser',
            'password': 'password'
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        token_key = response.data['token']
        token = ExpiringToken.objects.get(key=token_key)

        self.assertEqual(token.user, self.user)


    def test_signin_invalid_credentials(self):
        data = {
            'username': 'CustomUser',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.data['error'],
            'Invalid Credentials'
        )

        self.assertIn('error', response.data)
