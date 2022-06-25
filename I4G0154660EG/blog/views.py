from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy 
from .models import Post

#Create your views here.
def post_list_view(request):

    model = Post

    render(request, 'blog/post_list_view.html', {})

def post_create_view(request):

    model = Post
    fields ='__all__'
    success_url = reverse_lazy('blog:all')

    render(request, 'blog/post_form_view.html', {})

def post_detail_view(request):

    model = Post
    render(request, 'blog/post_detail_view.html', {})

def post_update_view(request):

    model = Post
    fields ='__all__'
    success_url = reverse_lazy('blog:all')

    render(request, 'blog/post_form_view.html', {})

def post_delete_view(request):

    model = Post
    fields ='__all__'
    success_url = reverse_lazy('blog:all')

    render(request, 'blog/post_delete_view.html', {})


 

      
       






