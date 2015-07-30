from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'login.views.login', name = 'user_login'),
    url(r'^accounts/auth/$', 'login.views.auth_view', name = 'user_login_auth'),
)
