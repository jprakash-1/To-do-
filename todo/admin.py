from django.contrib import admin
from .models import Todo

# Register your models here.

"""
    Class TodoAdmin is created to read the data from readonly part and pass it to admin. 
    Without this class we can not see the created field. 
"""

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo,TodoAdmin)
