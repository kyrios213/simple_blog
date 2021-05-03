from django.shortcuts import render
from django.views import generic

from .models import Post
from .forms import PostForm

class HomeView(generic.ListView):
    model = Post
    template_name = 'myblog/home.html'
    queryset = Post.objects.order_by('-id').all()


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'myblog/detail.html'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myblog/add_post.html'