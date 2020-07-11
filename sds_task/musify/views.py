from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from . import spotify as sp                     # Imported the spotify.py module.

# About page view method.
def about(request):
    return render(request, 'musify/about.html', {'title': 'About'})

@login_required                                 # Decorator used so that only authenticated user can view this page.
# Method for New Releases tab.
def home(request):
    r = {}
    if 'search' in request.GET:
            search_term =  request.GET['search']
            r = sp.client.search(search_term, "track")
            return render(request, 'musify/home.html', {'title': 'Home', 'data': r['tracks']['items'], "flag": "search"})

    else:
        r = sp.client.new_releases()
        return render(request, 'musify/home.html', {'title': 'Home', 'data': r["albums"]["items"], "flag": "new_releases"})

@login_required                                 # Decorator used so that only authenticated user can view this page.
# Method for Artists tab.
def home_search_artist(request):
    r = {}
    if 'search' in request.GET:
            search_term =  request.GET['search']
            r = sp.client.search(search_term, "artist")
            return render(request, 'musify/home_search_artist.html', {'title': 'Home', 'data': r['artists']['items'], "flag": "search"})

    else:
        r = sp.client.new_releases()
        return render(request, 'musify/home_search_artist.html', {'title': 'Home', 'data': r["albums"]["items"]})

@login_required                                 # Decorator used so that only authenticated user can view this page.
# Method for Playlists tab.
def home_search_playlist(request):
    r = {}
    if 'search' in request.GET:
            search_term =  request.GET['search']
            r = sp.client.search(search_term, "playlist")
            return render(request, 'musify/home_search_playlist.html', {'title': 'Home', 'data': r['playlists']['items'], "flag": "search"})

    else:
        r = sp.client.new_releases()
        return render(request, 'musify/home_search_playlist.html', {'title': 'Home', 'data': r["albums"]["items"]})

@login_required                                 # Decorator used so that only authenticated user can view this page.
# Method for Albums tab.
def home_search_album(request):
    r = {}
    if 'search' in request.GET:
            search_term =  request.GET['search']
            r = sp.client.search(search_term, "album")
            return render(request, 'musify/home_search_album.html', {'title': 'Home', 'data': r['albums']['items'], "flag": "search"})

    else:
        r = sp.client.new_releases()
        return render(request, 'musify/home_search_album.html', {'title': 'Home', 'data': r["albums"]["items"]})

@login_required                                 # Decorator used so that only authenticated user can view this page.
# Method for Pop tab.
def home_pop(request):
    r = {}
    if 'search' in request.GET:
            search_term =  request.GET['search']
            r = sp.client.search(search_term, "track")
            return render(request, 'musify/pop.html', {'title': 'Home', 'data': r['tracks']['items'], "flag": "search"})

    else:
        r = sp.client.get_category_playlists('pop')
        return render(request, 'musify/pop.html', {'title': 'Home', 'data': r["playlists"]["items"], "flag": "pop"})

@login_required                                 # Decorator used so that only authenticated user can view this page.
# Method for Party tab.
def home_party(request):
    r = {}
    if 'search' in request.GET:
            search_term =  request.GET['search']
            r = sp.client.search(search_term, "track")
            return render(request, 'musify/party.html', {'title': 'Home', 'data': r['tracks']['items'], "flag": "search"})

    else:
        r = sp.client.get_category_playlists('party')
        return render(request, 'musify/party.html', {'title': 'Home', 'data': r["playlists"]["items"], "flag": "party"})

@login_required                                 # Decorator used so that only authenticated user can view this page.
# Method for Hip-Hop tab.
def home_hiphop(request):
    r = {}
    if 'search' in request.GET:
            search_term =  request.GET['search']
            r = sp.client.search(search_term, "track")
            return render(request, 'musify/hiphop.html', {'title': 'Home', 'data': r['tracks']['items'], "flag": "search"})

    else:
        r = sp.client.get_category_playlists('hiphop')
        return render(request, 'musify/hiphop.html', {'title': 'Home', 'data': r["playlists"]["items"], "flag": "hiphop"})

@login_required                                 # Decorator used so that only authenticated user can view this page.
# Method for Bollywood tab.
def home_bollywood(request):
    r = {}
    if 'search' in request.GET:
            search_term =  request.GET['search']
            r = sp.client.search(search_term, "track")
            return render(request, 'musify/hiphop.html', {'title': 'Home', 'data': r['tracks']['items'], "flag": "search"})

    else:
        r = sp.client.get_category_playlists('bollywood')
        return render(request, 'musify/bollywood.html', {'title': 'Home', 'data': r["playlists"]["items"], "flag": "bollywood"})