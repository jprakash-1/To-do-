from django.contrib import admin
from .models import Todo,Profile,Feedback,Image

# Register your models here.

"""
    Class TodoAdmin is created to read the data from readonly part and pass it to admin. 
    Without this class we can not see the created field. 
"""
admin.site.register(Profile)
admin.site.register(Image)

class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Feedback,FeedbackAdmin)



class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo,TodoAdmin)
