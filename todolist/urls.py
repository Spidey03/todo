from django.conf.urls import url
from django.contrib import admin

from todolist.views.add_task import add_task
from todolist.views.add_task_confirm import add_task_confirm
from todolist.views.get_task import get_task
from todolist.views.get_todos import get_todos
from todolist.views.login import login
from todolist.views.login_confirm import login_confirm
from todolist.views.signup import signup
from todolist.views.signup_confirm import signup_confirm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup$', signup, name="SignUp"),
    url(r'^signup/confirm$', signup_confirm, name="SignUp"),
    url(r'^login$', login, name="Login"),
    url(r'^login/confirm$', login_confirm, name="LoginConfirm"),
    url(r'^tasks', get_todos, name="TodoList"),
    url(r'^add_task$', add_task, name="AddTask"),
    url(r'^add_task/confirm$', add_task_confirm, name="AddTaskConfirm"),
    url(r'^tasks/<int: task_id>/$', get_task, name="GetTask")
]