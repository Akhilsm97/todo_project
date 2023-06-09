from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=30)
    priority = models.CharField(max_length=30)
    task_date = models.DateField()

    def __str__(self):
        return self.task_name
