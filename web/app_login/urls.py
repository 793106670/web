__author__ = 'wenjiexu'

from django.contrib import admin
from django.conf.urls import patterns, url
from web.app_login.views import hello
from web.app_login.views import pagelogin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'/hello$', hello),
    url(r'/page$', pagelogin),
)

