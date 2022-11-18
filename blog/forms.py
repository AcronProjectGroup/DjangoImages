from django import forms

from .models import Post

class PostFormModel(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'status']