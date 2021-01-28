from django.urls import path
from .views import (PostListView, PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, file_share, SharedPostListView)
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='myApp-home'),
    path('shared/posts', SharedPostListView.as_view(), name='shared-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/share/', file_share, name='file-share'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')

]
