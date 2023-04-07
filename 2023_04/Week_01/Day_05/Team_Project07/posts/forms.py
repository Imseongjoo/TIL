from django import forms
from .models import Post


class PostForm(forms. ModelForm):
    title = forms.CharField(
        label='제목',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목',
                'max_length': 80,
                "class": "form-control",
                'style': 'width: 400px;'
            }
        ),
    )

    content = forms.CharField(
        label='내용',
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용',
                "class": "form-control",
                'style': 'width: 500px;'
            }
        ),
    )

    CATEGORY_CHOICES = [
        ('개발', '개발'),
        ('CS', 'CS'),
        ('신기술', '신기술')
    ]

    category = forms.ChoiceField(
        label='분류',
        label_suffix='',
        choices=CATEGORY_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select",
                'style': 'width: 100px;'
            }
        ),
    )

    class Meta:
        model = Post
        fields = '__all__'
