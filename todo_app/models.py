from django.db import models

# Create your models here.


class TaskModel(models.Model):
    task_description = models.CharField(max_length=200)
    is_done = models.BooleanField()

    def __str__(self):
        return self.task_description
