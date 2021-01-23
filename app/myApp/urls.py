from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='myApp-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create')

]
