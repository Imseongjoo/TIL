from django import forms
from .models import Review, Comment
from django.forms.widgets import ClearableFileInput


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'movie': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'image': ClearableFileInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
        }


class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'movie': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
            'image': ClearableFileInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}),
        }
