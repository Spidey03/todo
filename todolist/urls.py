from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from todolist import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'signup/', views.signup, name="SignUp"),
    path(r'signup/confirm/', views.signup_confirm, name="SignUp"),
    path(r'login/', views.login, name="Login"),
    path(r'login/confirm/', views.login_confirm, name="LoginConfirm"),
    path(r'profile/', views.get_profile, name="Profile"),
    path(r'tasks/', views.get_tasks, name="TodoList"),
    path(r'tasks/task/<int:task_id>/update/', views.update_task, name="UpdateTask"),
    path(r'tasks/category/<int:category_id>/',
         views.get_task_filter_by_category,
         name="TodoListByCategory"),
    path(r'tasks/lable/<int:lable_id>/', views.get_task_filter_by_lable,
         name="TodoListByCategory"),
    path(r'add_task/', views.add_task, name="AddTask"),
    path(r'add_task/confirm/', views.add_task_confirm, name="AddTaskConfirm"),
    path(r'tasks/task/<int:task_id>/', views.get_task, name="GetTask")
]
