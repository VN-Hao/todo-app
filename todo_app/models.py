from django.db import models

# Create your models here.


class TaskModel(models.Model):
    task_description = models.CharField(max_length=200)
    is_done = models.BooleanField()
    username = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.task_description
    

class UserModel(models.Model):
    username = models.CharField(max_length=50)
    hashed_password = models.CharField(max_length=100) 

    def __str__(self):
        return self.username
