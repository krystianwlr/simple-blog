"""Defines URL patterns for blog_engine"""

from django.conf.urls import url

from . import views

app_name = 'blog_engine'

urlpatterns = [
    #Post list
    url(r'^$', views.post_list, name='post_list'),

    #Single post
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),

    #New post
    url(r'^post/new/$', views.post_new, name='post_new'),

    #Post edit
    url(r'^post/(?P<post_id>\d+)/edit/$', views.post_edit, name='post_edit')
]