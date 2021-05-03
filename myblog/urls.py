from django.urls import path
from .views import HomeView, PostDetailView, PostCreateView

app_name = 'myblog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
]