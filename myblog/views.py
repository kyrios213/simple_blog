from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm, EditForm

class HomeView(generic.ListView):
    model = Post
    template_name = 'myblog/home.html'
    queryset = Post.objects.order_by('-post_date').all()


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'myblog/detail.html'


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myblog/add_post.html'


class PostEditView(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'myblog/update_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'myblog/delete_post.html'
    success_url = reverse_lazy('myblog:home')