from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=30, required=True
    )
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(),
    )
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]