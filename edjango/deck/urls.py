from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'deck.views.deck_home', name = 'deck_home'),
)
