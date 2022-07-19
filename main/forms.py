from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import SimpleFinding


class SimpleFindingForm(forms.Form):
    sn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Серийный номер'}), max_length=30, required=False)
    secretnum = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Секретный номер'}), max_length=30, required=False)
    mark = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Марка'}), max_length=30, required=False)

    class Meta:
        model = SimpleFinding
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
