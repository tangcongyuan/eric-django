from django.conf.urls import patterns, url

urlpatterns = patterns('',
    #url(r'^$', 'accounts.views.accounts_home', name = 'accounts_home'),
    url(r'^login/$', 'accounts.views.login', name = 'player_login'),
    url(r'^logout/$', 'accounts.views.logout', name = 'player_logout'),
    url(r'^loggedIn/$', 'accounts.views.loggedIn', name = 'player_loggedIn'),
)
