from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} {self.name}'


class Label(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class UserTask(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    lable = models.ManyToManyField(Label, through='TaskLable')
    date = models.DateField(default=datetime.today)
    editable = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    stage = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.content}'


class TaskLable(models.Model):
    lable = models.ForeignKey(Label, on_delete=models.CASCADE)
    task = models.ForeignKey(UserTask, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task.title}'


class User(AbstractUser):
    email = models.EmailField('email address', unique=True, null=False)
    profile_pic = models.CharField(max_length=3000)
    bio = models.CharField(max_length=200)
