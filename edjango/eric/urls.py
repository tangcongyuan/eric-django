from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'eric.views.eric', name = 'eric_home'),
)
