from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField( default=timezone.now)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'todos', default=1)

    def __str__(self):
        return self.title