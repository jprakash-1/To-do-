from django.forms import ModelForm
from .models import Todo

"""
    Created todo form to take data from webpage using this form.

"""

class TodoForm(ModelForm):
    class Meta :
        model = Todo
        fields = ['title','memo','important']