from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Todo,Profile,Feedback

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

class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class FeedbackForm(ModelForm):
    class Meta :
        model = Feedback
        fields = ['email','title','feedback']