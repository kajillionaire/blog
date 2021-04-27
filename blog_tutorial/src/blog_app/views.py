from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy

from .models import Post, Comment


class HomePageView(ListView):
    model = Post
    template_name = 'homepage.html'
    context_object_name = 'all_blogs_list'

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_blogs_list'

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'blog_details.html'
    login_url = 'login'


class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'author' , 'body']
    login_url = 'login'



class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']
    login_url = 'login'

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user
    
class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): 
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    login_url = 'login'   

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user

# Create your views here.
