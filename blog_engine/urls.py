"""Defines URL patterns for blog_engine"""

from django.conf.urls import url

from . import views

app_name = 'blog_engine'

urlpatterns = [
    #Post list
url(r'^$', views.post_list, name='post_list'),
]