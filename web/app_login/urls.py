__author__ = 'wenjiexu'

from django.contrib import admin
from django.conf.urls import patterns, url
from web.app_login.views import hello
from web.app_login.views import pagelogin
from web.app_login.views import display_user

admin.autodiscover()

urlpatterns = patterns('',
    url(r'/hello$', hello),
    url(r'/login$', pagelogin),
    url(r'/showuser$', display_user)
)

