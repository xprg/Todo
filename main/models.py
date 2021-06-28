from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='prg1',related_name='todolist')
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todo=models.ForeignKey(TodoList,on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    done=models.BooleanField()

    def __str__(self):
        return self.text
    
        
    