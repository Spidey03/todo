from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} {self.name}'


class Lable(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    lable = models.ManyToManyField(Lable, through='TaskLable')
    date = models.DateField()

    def __str__(self):
        return f'{self.title} {self.content}'


class TaskLable(models.Model):
    lable = models.ForeignKey(Lable, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task.title}'