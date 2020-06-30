from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from . import spotify as sp

@login_required
def home(request):
    r = {}
    if 'search' in request.GET:
            search_term =  request.GET['search']
            r = sp.client.search(search_term, "artist")
    return render(request, 'musify/home.html', {'title': 'Home', 'data': r['artists']['items']})

# class PostListViewVolunteer(ListView):
#     model = Post
#     template_name = 'musify/home.html'   #<app>/<model>_<viewtype>.html
    
#     def get(self, request):
        
#         if 'search' in request.GET:
#             search_term =  request.GET['search']
#             # posts = posts.filter(Q(title__icontains = search_term) | 
#             #                      Q(content__icontains = search_term))
#         search_term = ''
                                 
#         return redirect('home')

def about(request):
    return render(request, 'musify/about.html', {'title': 'About'})
