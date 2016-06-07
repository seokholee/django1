from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
        url(r'^signup/$', views.signup, name='signup'),
]
