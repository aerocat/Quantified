from django.conf.urls import url
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
]
