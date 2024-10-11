from django.contrib import admin
from django.urls import path, include
from platform_app.views import ChannelView, ChannelContentView, ContentView, SubChannelView
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('contents/<content_id>', ContentView.as_view(), name='content'),
    path('channels/contents/<channel_id>', ChannelContentView.as_view(), name='channel_contents'),
    path('channels/', ChannelView.as_view(), name='channel'),
    path('channels/<channel_id>', SubChannelView.as_view(), name='channel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)