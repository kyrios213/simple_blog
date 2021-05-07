from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Post, Category
from .forms import PostForm, EditForm, CategoryForm

class HomeView(generic.ListView):
    model = Post
    template_name = 'myblog/home.html'
    queryset = Post.objects.order_by('-id').all()

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'myblog/detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myblog/add_post.html'


class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForm
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
    cat_menu = Category.objects.all()
    category = Category.objects.filter(name=cats.replace('-', ' ')).first()
    post = Post.objects.filter(category=category).order_by('-id')
    return render(request, 'myblog/categories.html', {
        'post_categories': post, 
        'category': category,
        'cat_menu': cat_menu,
        })

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'myblog/category_list.html', {
        'cat_menu_list': cat_menu_list,
    })