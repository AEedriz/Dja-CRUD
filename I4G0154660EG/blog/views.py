from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy 
from .models import Post

#Create your views here.
class PostDetailViews(generic.DetailView):
    model = Post

class PostListViews(generic.ListView):
    model = Post
    fields = "__all__"
    success_url= reverse_lazy('blog:all')

class PostCreateViews(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url= reverse_lazy('blog:all')

class PostUpdateViews(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url= reverse_lazy('blog:all')

class PostDeleteViews(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url= reverse_lazy('blog:all')




 

      
       






