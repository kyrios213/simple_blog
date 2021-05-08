from django.urls import path
from .views import HomeView, PostDetailView, PostCreateView, PostEditView, PostDeleteView, CategoryCreateView, CategoryView, CategoryListView, LikeView

app_name = 'myblog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('add_category/', CategoryCreateView.as_view(), name='category'),
    path('article/edit/<int:pk>', PostEditView.as_view(), name='edit'),
    path('article/delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('category/<str:cats>/', CategoryView, name='categoryview'),
    path('category_list/', CategoryListView, name='categorylist'),
    path('like/<int:pk>', LikeView, name='like_post'),
]