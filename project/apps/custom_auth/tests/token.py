from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.custom_auth.models import ExpiringToken
from apps.users.models import CustomUser


class TokenDeleteViewTest(APITestCase):
    url = reverse('token-delete')

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password',
            email='testuser@example.com',
            phone='+994702215209'
        )
        self.token = ExpiringToken.objects.create(user=self.user)

    def test_delete_token(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {'message': 'Token deleted successfully'}
        )
        self.assertFalse(
            ExpiringToken.objects.filter(user=self.user).exists()
        )

    def test_unauthenticated_request(self):
        response = self.client.delete(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.assertEqual(
            response.data,
            {'detail': 'Authentication credentials were not provided.'}
        )

        self.assertTrue(
            ExpiringToken.objects.filter(user=self.user).exists())
