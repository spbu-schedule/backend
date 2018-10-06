from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('mainApp.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^search/', include('search.urls')),
]
