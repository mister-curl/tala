from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tala/api/v1/', include('api.urls', namespace='api')),
    url(r'^ui/', include('webui.urls')),
]
