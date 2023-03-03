from django.urls import path
from apps.custom_auth.apis import *

urlpatterns = [

    path('sign-in', SignInView.as_view(), name='signin'),
    path('sign-up', SignUpView.as_view(), name='signup'),
    path('token', TokenDeleteView.as_view(), name='token-delete'),
]
