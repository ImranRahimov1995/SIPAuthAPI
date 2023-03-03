from django.urls import path
from apps.users.apis import *

urlpatterns = [
    path('info', UserInfoAPIView.as_view(), name='info'),
]
