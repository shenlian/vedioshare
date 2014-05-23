# coding: UTF-8
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView,ListView


urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'},name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'registration/logout.html'},name='auth_logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'registration/password_change_form.html'},name='auth_password_change'),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'registration/password_change_done.html'},name='auth_password_change_done'),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'registration/password_change_done.html'},name='auth_password_change_done'),
)
