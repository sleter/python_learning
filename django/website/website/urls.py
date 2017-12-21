from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'music/', include('music.urls')),
]
