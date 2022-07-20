from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import SimpleFinding, AddNotes


class SimpleFindingForm(forms.Form):
    sn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Серийный номер'}), max_length=30, required=False)
    secretnum = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Секретный номер'}), max_length=30, required=False)
    mark = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Марка'}), max_length=30, required=False)

    class Meta:
        model = SimpleFinding
        fields = '__all__'


class AddNotesForm(forms.Form):

    question_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Номер для запроса'}), max_length=30)
    date_fld = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control item', 'placeholder': 'Дата вопроса'}))
    name_fld = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'ФИО'}), max_length=30, required=False)
    organization_fld = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Организация'}), max_length=30, required=False)
    telephone_fld = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control item', 'placeholder': 'Телефон'}), max_length=30, required=False)
    question_fld = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control item', 'placeholder': 'Вопрос'}), max_length=30)
    add_notes_fld = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control item', 'placeholder': 'Дополнения'}), max_length=30, required=False)

    class Meta:
        model = AddNotes
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
