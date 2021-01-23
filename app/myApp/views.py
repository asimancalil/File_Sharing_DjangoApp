from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


def home(request):
    context ={
        'posts': Post.objects.get(author=request.user.username)
    }
    return render(request, 'myApp/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'myApp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['file_field', 'desc']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#
# def new_post(request):
#     template = 'myApp/post_form.html'
#     form = PostForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('post-detail')
#     else:
#         form = PostForm()
#     context = {
#         'form': form,
#     }
#     return render(request, template, context)