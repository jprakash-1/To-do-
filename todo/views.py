from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def home(request):
    return render(request,'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request,'todo/signupuser.html',{'forms':UserCreationForm()})
    else :
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                user.save()
                # When user signed in redirect to new url.
                login(request,user)
                return redirect('current')

            except IntegrityError:
                return render(request,'todo/signupuser.html',{'forms':UserCreationForm(),'error':'Username is already taken try other!'})

        else:
            # Tell the use user password didn't match.
            return render(request,'todo/signupuser.html',{'forms':UserCreationForm(),'error':'Password did not match'})


def current(request):
    return render(request,'todo/current.html')

def logoutuser(request):
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request,'todo/loginuser.html',{'forms':AuthenticationForm()})
    else :
        user = authenticate(request,username = request.POST['username'],password = request.POST['password'])
        if user is None:
            return render(request,'todo/loginuser.html',{'forms':AuthenticationForm(),'error':'Username and password did not match'})
        else :
            login(request,user)
            return redirect('home')