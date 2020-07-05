from django.urls import path
from . import views

# URL patterns for about, new-releases, pop, party, hiphop, bollywood and various search pages.
urlpatterns = [
    path('home/', views.home, name='home'),
    path('pop/', views.home_pop, name='home-pop'),
    path('party/', views.home_party, name='home-party'),
    path('hiphop', views.home_hiphop, name='home-hiphop'),
    path('bollywood', views.home_bollywood, name='home-bollywood'),
    path('search/artist', views.home_search_artist, name='home-search-artist'),
    path('search/playlist', views.home_search_playlist, name='home-search-playlist'),
    path('search/album', views.home_search_album, name='home-search-album'),
    path('about/', views.about, name='musify-about'),
]