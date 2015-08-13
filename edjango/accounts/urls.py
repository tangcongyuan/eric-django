from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'accounts.views.login', name = 'user_login'),
    url(r'^auth/$', 'accounts.views.auth_view', name = 'user_login_auth'),
)
