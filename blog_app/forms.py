from django import forms
from django.forms import fields, widgets
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
        exclude = ('user', 'date')

        widgets = {
            'Blog_Title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'Blog_Description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'blog_content': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'blog_image': forms.FileInput(attrs={
                'class': 'form-control'
            })

        }
