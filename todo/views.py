from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signupuser(request):
    return render(request,'todo/signupuser.html',{'forms':UserCreationForm()})