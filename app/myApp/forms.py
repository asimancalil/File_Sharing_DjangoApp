from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['desc', 'file_field']


class FileShareForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['share']