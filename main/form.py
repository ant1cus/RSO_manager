from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import SimpleFinding, AddNotes


class AddNotesForm(forms.Form):

    question_number_fld = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Номер для запроса'}), min_length=5, max_length=30)
    date_fld = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control item', 'placeholder': 'Дата вопроса'}))
    name_fld = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'ФИО'}), max_length=30, required=False)
    organization_fld = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Организация'}), max_length=30, required=False)
    telephone_fld = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Телефон'}), max_length=30, required=False)
    question_fld = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control item', 'placeholder': 'Вопрос'}))
    add_notes_fld = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control item', 'placeholder': 'Дополнения'}), required=False)

    class Meta:
        model = AddNotes
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Логин'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control item', 'placeholder': 'Почта'}), max_length=64,
                             help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control item', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control item', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
