from django.contrib import admin
from .models import Task, Chat

@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display=('text', 'answer')

@admin.register(Chat)
class Chat(admin.ModelAdmin):
    list_display=('username', 'token')