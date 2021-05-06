from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Post, Category
from .forms import PostForm, EditForm

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


class CategoryCreateView(generic.CreateView):
    model = Category
    fields = '__all__'
    template_name = 'myblog/add_category.html'


class PostEditView(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'myblog/update_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'myblog/delete_post.html'
    success_url = reverse_lazy('myblog:home')

def CategoryView(request, cats):
    category = Category.objects.filter(name=cats).first()
    post = Post.objects.filter(category=category).order_by('-id')
    return render(request, 'myblog/categories.html', {'post_categories': post, 'category': category,})