from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='index'),
]