from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Todo

"""
    Created todo form to take data from webpage using this form.

"""

class TodoForm(ModelForm):
    class Meta :
        model = Todo
        fields = ['title','memo','important']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']