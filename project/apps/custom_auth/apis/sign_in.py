from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import authenticate
from rest_framework.permissions import AllowAny

from apps.custom_auth.models import ExpiringToken
from apps.users.serializers import UserAuthSerializer


class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            **serializer.data
        )
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=400)

        token, created = ExpiringToken.objects.get_or_create(user=user)

        return Response({'token': token.key})
