from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.users.serializers import UserSerializer


class UserInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: "user",
            400: "Bad request"
        }
    )
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            200: "user",
            400: "Bad request"
        }
    )
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user,
                                    data=request.data,
                                    partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {'user': serializer.data},
                status=200
            )

        return Response(serializer.errors, status=400)
