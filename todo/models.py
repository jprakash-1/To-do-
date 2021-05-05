from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

"""
    Here This is a todo model with all necessary fields required. Created field is completed automatically
    with date time value that cannot be modified by the user.

    ForeignKey to link this model with user model this is one to many as one user can have several todos.
    

"""

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    

class Feedback(models.Model):
    email = models.EmailField(max_length = 254)
    title = models.CharField(max_length=100)
    feedback = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    