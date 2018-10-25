from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.search,name = 'search'),
    url(r'^time/$', views.time,name = 'time')
]
