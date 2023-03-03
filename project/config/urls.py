from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.users.apis import LatencyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/latency', LatencyAPIView.as_view(), name='latency'),
    path('api/auth/', include('apps.custom_auth.urls')),
    path('api/users/', include('apps.users.urls')),

]

# Local settings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
