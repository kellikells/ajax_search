from django.conf.urls import url
from . import views         

urlpatterns = [
    url(r'^$', views.index),

    url(r'^create/$', views.create),

    url(r'^show/$', views.show),

    url(r'^search/$', views.search),

    # url(r'^/$', views.),

    # url(r'^/$', views.),

    # url(r'^/$', views.),

    # url(r'^/$', views.),

    # url(r'^/$', views.),





]
