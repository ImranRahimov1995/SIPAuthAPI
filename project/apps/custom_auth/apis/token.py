from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class TokenDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        request.user.auth_token.delete()

        return Response({"message": "Token deleted successfully"},
                        status=status.HTTP_200_OK)
