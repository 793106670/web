#! -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #r的含义 它告诉Python这是个原始字符串，不需要处理里面的反斜杠（转义字符）。
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', include('web.app_login.urls')),
)
