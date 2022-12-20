from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.core.validators import RegexValidator
from location.views import *

urlpatterns = [
    url(r'^location_query/$', location_query),
    path('location_query_content/<str:csv>/',location_query_content,name = 'location_query_content'),
    url(r'^location_create/$', location_create),
    path('location_create_content/<str:csv>/',location_create_content,name = 'location_create_content')
]
