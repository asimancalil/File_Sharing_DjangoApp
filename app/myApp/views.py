from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib import messages
from .forms import FileShareForm
from django.contrib.auth.models import User


def home(request):
    context ={
        'posts': Post.objects.get(author=request.user.username)
    }
    return render(request, 'myApp/home.html', context)


class SharedPostListView(ListView):
    template_name = 'myApp/shared_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        share = self.request.user.pk
        post = Post.objects.get(share=share)
        messages.success(self.request, f'{post.author} shared this file with you!')
        return Post.objects.filter(share=share).order_by('-date_posted')


class PostListView(ListView):
    # model = Post
    template_name = 'myApp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        author = self.request.user
        return Post.objects.order_by().filter(author=author).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['file_field', 'desc']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def file_share(request, pk):
    form = FileShareForm(request.POST or None)
    post = Post.objects.get(id=pk)

    if request.user.is_authenticated and post.author == request.user:
        if form.is_valid():
            shared_user_id = request.POST.get('share')
            post.share.add(shared_user_id)

    context = {
        'form': form,
    }
    template = 'myApp/file_share.html'
    messages.success(request, f'Your file has been shared ')
    return render(request, template, context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Post
    fields = ['file_field', 'desc']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

