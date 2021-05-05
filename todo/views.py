from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import TodoForm,UserRegistrationForm,UserUpdateForm,ProfileUpdateForm,FeedbackForm,ImageForm
from .models import Todo
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required           # this will make sure that we need to login to use this function.


# Create your views here.

def home(request):
    return render(request,'todo/home.html')

def signupuser(request):
    # Here we get into signup page didn't filled the detail and submit it.
    if request.method == 'GET':
        return render(request,'todo/signupuser.html',{'forms':UserRegistrationForm()})
    else :
        # Here we get into signup page did fill the detail and submit it.
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'],email = request.POST['email'])
                user.save()             # Save the user detail in the database
                # When user signed in redirect to new url.
                login(request,user)
                return redirect('about')

            # Check Weather username is unique or not. 
            except IntegrityError:     
                return render(request,'todo/signupuser.html',{'forms':UserRegistrationForm(),'error':'Username is already taken try other!'})

        else:
            # Tell the use user password didn't match.
            return render(request,'todo/signupuser.html',{'forms':UserRegistrationForm(),'error':'Password did not match'})


def about(request):
    return render(request,'todo/about.html')

@login_required
def logoutuser(request):
        logout(request)                                    # Creating a logout request. 
        return redirect('home')                            # Redirecting it to home page.

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


"""
    Creating createtodo  

"""

@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request,'todo/createtodo.html',{'forms':TodoForm()})
    else :
        try :
            form = TodoForm(request.POST)           # Put all the data we get from webpage 
            newtodo = form.save(commit=False)       # commit = False means don't save to database yet and create newtodo object to copy form object value.
            newtodo.user = request.user             # here in new object populating the user name that is logged in. 
            newtodo.save()                          # Saving the value.
            return redirect('current')
        except ValueError :
            return render(request,'todo/createtodo.html',{'forms':TodoForm(),'error':"Bad Data Try Again !"})

@login_required
def current(request):   
    todos = Todo.objects.filter(user=request.user,datecompleted__isnull = True)          # select the todo list of user logged in. 
    return render(request,'todo/current.html', {'todos':todos})


@login_required
def completedtodos(request):   
    todos = Todo.objects.filter(user=request.user,datecompleted__isnull = False).order_by('-datecompleted')          # select the todo list of user logged in. 
    return render(request,'todo/completedtodos.html', {'todos':todos})


@login_required
def viewtodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk = todo_pk,user = request.user)         # Get object or return 404
    if  request.method == 'GET':
        form = TodoForm(instance=todo)                                      # instance = todo means fill the data in form that was available in todo
        return render(request,'todo/viewtodo.html', {'todo':todo,'form':form})    
    else :
        try:
            form = TodoForm(request.POST,instance=todo)                     # Update the todo form and save it.
            form.save()
            return redirect('current')
        except ValueError():
            return render(request,'todo/viewtodo.html', {'todo':todo,'form':form,'error': "Bad Data Try Again !"}) 



@login_required
def completetodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk = todo_pk,user = request.user) 
    if  request.method == 'POST':
        # current time has been stored as we put timezone.now() in datecompleted part.
        todo.datecompleted = timezone.now()             # As we are checking Completed todo from their time completed.
        todo.save()
        return redirect('current')



@login_required
def deletetodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk = todo_pk,user = request.user) 
    if  request.method == 'POST':
        todo.delete()                           # Delete the data from database.
        return redirect('current')

@login_required
def profile(request):
    return render(request,'todo/profile.html')

@login_required
def profileUpdate(request):
    if  request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated !')
            return redirect('profile')
        else :
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

            context = {
                'u_form':u_form,
                'p_form':p_form
            }
            return render(request,'todo/profileUpdate.html',context,{'error':'Bad Data ! Try Again' })

    else :
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form':u_form,
            'p_form':p_form
        }
        return render(request,'todo/profileUpdate.html',context)

@login_required
def feedback(request):
    if request.method == 'GET':
        return render(request,'todo/feedback.html',{'form':FeedbackForm()})
    else :
        try :
            form = FeedbackForm(request.POST)           # Put all the data we get from webpage 
            newtodo = form.save()                             # Saving the value.
            return redirect('home')
        except ValueError :
            return render(request,'todo/feedback.html',{'form':FeedbackForm(),'error':"Bad Data Try Again !"})


def imageupload(request):
    if request.method == 'GET':
        return render(request,'todo/imageupload.html',{'form':ImageForm()})    
    else :
        try :
            form = ImageForm(request.POST,request.FILES)           # Put all the data we get from webpage 
            newtodo = form.save()                             # Saving the value.
            return redirect('home')
        except ValueError :
            return render(request,'todo/imageupload.html',{'form':ImageForm(),'error':"Bad Data Try Again !"})
