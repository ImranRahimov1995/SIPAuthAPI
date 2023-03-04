from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema

from apps.custom_auth.models import ExpiringToken
from apps.users.serializers import UserSignUpSerializer


class SignUpView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=UserSignUpSerializer,
        responses={
            200: "token",
            400: "Bad request"
        }
    )
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = ExpiringToken.objects.get_or_create(user=user)

        return Response({'token': token.key})
