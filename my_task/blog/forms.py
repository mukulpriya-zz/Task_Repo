from django import forms
from django.forms import ModelForm
from blog.models import *

class BlogPostForm(ModelForm):
    class Meta:
        model = Blog_Post
        fields =('title','body',)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
        