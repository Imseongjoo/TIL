from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        label_suffix = ''

    username = forms.CharField(label='아이디', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    email = forms.EmailField(label='이메일', label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'style': 'width: 250px;'}))
    password1 = forms.CharField(label='비밀번호', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    password2 = forms.CharField(label='비밀번호 확인', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'width: 200px;'}))


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)
        label_suffix = ''

    email = forms.EmailField(label='이메일', label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'style': 'width: 250px;'}))
    password = None


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="아이디",
        label_suffix='',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width: 250px;'})
    )

    password = forms.CharField(
        label="비밀번호",
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'style': 'width: 250px;'})
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="기존 비밀번호",
        label_suffix='',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'style': 'width: 250px;'})
    )

    new_password1 = forms.CharField(
        label="새로운 비밀번호",
        label_suffix='',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'style': 'width: 250px;'})
    )

    new_password2 = forms.CharField(
        label="새로운 비밀번호 확인",
        label_suffix='',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'style': 'width: 250px;'})
    )
