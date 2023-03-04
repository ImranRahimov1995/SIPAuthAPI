import subprocess

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema


class LatencyAPIView(APIView):
    @swagger_auto_schema(
        responses={
            200: "70 ms",
            400: "Failed to get latency from google.com"
        }
    )
    def get(self, request):

        ping_host = 'google.com'

        ping_result = subprocess.run(
            ['ping', '-c', '1', ping_host],
            capture_output=True,
            text=True
        )

        for line in ping_result.stdout.split('\n'):
            if 'rtt' in line:
                latency = line.split('=')[1].split('/')[1]
                return Response(
                    {
                        'latency': f"{round(float(latency))} ms"
                    }
                )

        return Response(
            {
                'error': 'Failed to get latency from ' + ping_host
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
