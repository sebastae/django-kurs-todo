from django.contrib import admin

# Register your models here.
from list.models import TodoItem

admin.site.register(TodoItem)