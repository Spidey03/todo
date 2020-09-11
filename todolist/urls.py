from django.conf.urls import url
from django.contrib import admin

from todolist.views.add_task import add_task
from todolist.views.add_task_confirm import add_task_confirm
from todolist.views.get_todos import get_todos

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_todos, name="TodoList"),
    url(r'^add_task$', add_task, name="AddTask"),
    url(r'^add_task/confirm$', add_task_confirm, name="AddTaskConfirm"),
]