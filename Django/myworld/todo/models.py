

# Create your models here.
from django.db import models
#import datetime

class Todolist(models.Model):
  todoitem = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  deleted_at = models.DateTimeField(auto_now=True)
