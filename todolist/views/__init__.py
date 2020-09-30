from todolist.views.add_task import add_task
from todolist.views.add_task_confirm import add_task_confirm
from todolist.views.get_profile import get_profile
from todolist.views.get_task import get_task
from todolist.views.get_tasks import get_tasks
from todolist.views.get_tasks_filter_by_category import \
    get_task_filter_by_category
from todolist.views.get_tasks_filter_by_lable import get_task_filter_by_lable
from todolist.views.login import login
from todolist.views.login_confirm import login_confirm
from todolist.views.signup import signup
from todolist.views.signup_confirm import signup_confirm
from todolist.views.update_task import update_task

__all__ = ["add_task", "add_task_confirm", "get_profile", "get_task",
           'get_tasks', "get_task_filter_by_category",
           "get_task_filter_by_lable", "login", 'login_confirm', "signup",
           "signup_confirm", "update_task"]

