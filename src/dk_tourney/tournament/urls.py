from django.conf.urls import patterns, include, url

from tournament.views import TournamentListView, GameListView, GameDetailView, interest_in_game

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^tournaments/$', TournamentListView.as_view(), {}, 'tournament_list'),
    url(r'^games/$', GameListView.as_view(), {}, 'game_list'),

    url(r'^games/(?P<pk>\d+)/$', GameDetailView.as_view(), {}, 'game_detail'),
    url(r'^games/(?P<pk>\d+)/interested$', interest_in_game, {}, 'game_interest_added'),
)

