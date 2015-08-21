__author__ = 'SuturkinAA'

from django.conf.urls import include, url
from django.contrib import admin
from rest import views

urlpatterns = [
    url(r'^allocate/[a-zA-Z0-9]+[/]?$', views.allocate),
    url(r'^deallocate/[r]{1}[0-9]+[/]?$', views.deallocate),
    url(r'^deallocate/[a-zA-z0-9]+[/]?$', views.deallocateByName),
    url(r'^list[/]?$', views.list),
    url(r'^list/[a-zA-z0-9]+[/]?$', views.listByName),
    url(r'^reset[/]?$', views.reset),

    url(r'', views.badRequest),
]
