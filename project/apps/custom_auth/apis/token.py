from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema


class TokenDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        responses={
            200: "Token deleted successfully",
            400: "Invalid token"
        }
    )
    def delete(self, request, *args, **kwargs):
        request.user.auth_token.delete()

        return Response({"message": "Token deleted successfully"},
                        status=status.HTTP_200_OK)
