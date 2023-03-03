from typing import Tuple

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from apps.custom_auth.models import ExpiringToken


class ExpiringTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"

    def authenticate_credentials(self, key) -> Tuple:
        try:
            token = ExpiringToken.objects.get(key=key)

        except self.get_model().DoesNotExist:
            raise AuthenticationFailed('Invalid Token')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted')

        if token.has_expired():
            token.delete()
            raise AuthenticationFailed('Token has expired')

        token.update_lifetime()

        return token.user, token
