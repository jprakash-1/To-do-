from django.contrib import admin
from .models import Todo,Profile

# Register your models here.

"""
    Class TodoAdmin is created to read the data from readonly part and pass it to admin. 
    Without this class we can not see the created field. 
"""
admin.site.register(Profile)

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo,TodoAdmin)
