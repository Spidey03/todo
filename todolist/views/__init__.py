from todolist.views.add_task import add_task
from todolist.views.get_profile import get_profile
from todolist.views.get_task import get_task
from todolist.views.get_tasks import get_tasks, get_tasks_filter_by_category, \
    get_tasks_filter_by_lable
from todolist.views.login import login
from todolist.views.login_confirm import login_confirm
from todolist.views.signup import signup
from todolist.views.signup_confirm import signup_confirm
from todolist.views.update_task import update_task

__all__ = ["add_task", "get_profile", "get_task",
           'get_tasks', "login", 'login_confirm', "signup",
           "signup_confirm", "update_task"]

