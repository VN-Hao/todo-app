from django.contrib import admin
from .models import TaskModel, UserModel

# Register your models here.

admin.site.register(TaskModel)
admin.site.register(UserModel)