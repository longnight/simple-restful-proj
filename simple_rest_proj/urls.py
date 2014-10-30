from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest.views import rest_index, rest_id

urlpatterns = patterns('',    
    url(r'^rest$', rest_index, name="index"),
    url(r'^rest/(?P<id>[\d]+)$', rest_id, name="id"),
)
