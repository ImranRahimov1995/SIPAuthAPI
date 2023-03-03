import json

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import CustomUser
from apps.custom_auth.models import ExpiringToken


class UserInfoAPIViewTest(APITestCase):
    url = reverse('info')

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password',
            email='testuser@example.com',
            phone='+994702215209'
        )
        self.token = ExpiringToken.objects.create(user=self.user)

    def test_get_user_info(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(response.data.keys()),
            {'username', 'phone', 'email', 'date_joined'}
        )
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['phone'], self.user.phone)
        self.assertEqual(response.data['email'], self.user.email)
        self.assertIsNotNone(response.data['date_joined'])

    def test_update_user_info(self):
        new_phone = '+994702215209'
        email = "changed@mail.com"

        self.client.force_authenticate(user=self.user)
        data = {
            'phone': new_phone,
            'email': email
        }

        response = self.client.put(self.url,
                                   json.dumps(data),
                                   content_type="application/json")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            set(response.data.keys()),
            {'user'}
        )

        self.assertEqual(response.data['user']['phone'], new_phone)
        self.assertEqual(response.data['user']['email'], email)
        self.assertEqual(self.user.phone, new_phone)

    def test_partial_update_user_info(self):
        new_phone = '+994775005050'

        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.url,
                                   json.dumps({'phone': new_phone}),
                                   content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(response.data.keys()),
            {'user'}
        )
        self.assertEqual(response.data['user']['phone'], new_phone)
        self.assertEqual(self.user.phone, new_phone)

    def test_unauthenticated_request(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data, {
                'detail': 'Authentication credentials were not provided.'
            }
        )
