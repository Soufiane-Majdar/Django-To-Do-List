from pyexpat import model
from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.TextField()
    Completed=models.BooleanField()

    def __str__(self):
        return self.task
