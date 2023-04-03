from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '제목 입력'}),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={'class': 'my-content'}),
        required=False,
    )
    priority = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 1, 'max': 5, 'value': 3}),
        initial=3,
    )
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
    )

    class Meta:
        model = Todo
        fields = ['title', 'content', 'completed', 'priority', 'deadline']
