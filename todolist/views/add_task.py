from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from todoapp.settings import LOGIN_REDIRECT_URL
from todolist import utils


@login_required(login_url=LOGIN_REDIRECT_URL)
def add_task(request):
    categories = utils.get_all_categories()
    lables = utils.get_all_lables()
    context = {
        "title": {
            "name": "Home",
            "url": "/tasks"
        },
        "categories": categories,
        "lables": lables
    }
    return render(request, "add_task.html", context)

