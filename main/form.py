from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import SimpleFinding


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Логин'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control item', 'placeholder': 'Почта'}), max_length=64,
                             help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control item', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control item', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
