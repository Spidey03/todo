from django.contrib import admin

# Register your models here.
from todolist.models import Category, Lable, Task, TaskLable

admin.site.register(Category)
admin.site.register(Lable)
admin.site.register(Task)
admin.site.register(TaskLable)