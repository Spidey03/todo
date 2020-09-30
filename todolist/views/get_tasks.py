from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from todoapp.settings import LOGIN_REDIRECT_URL


@login_required(login_url=LOGIN_REDIRECT_URL)
def get_tasks(request):
    user_id = request.user.id
    from todolist.storages.storage_implementation \
        import StorageImplementation
    from todolist.presenters.presenter_implementation \
        import PresenterImplementation
    presenter = PresenterImplementation()
    storage = StorageImplementation()
    from todolist.interactors.get_tasks import GetTasks
    interactor = GetTasks(storage=storage, presenter=presenter)
    tasks = interactor.get_tasks_wrapper(user_id=user_id)
    # TODO: IMPLEMENT GET USER
    from todolist.models import User
    user = User.objects.get(id=user_id)
    # TODO: IMPLEMENT GET CATEGORY
    categories = storage.get_all_categories()
    # TODO: IMPLEMENT GET LABLE
    from todolist.models import Lable
    lables = Lable.objects.all()
    context = {
        "title":{
            "name": "Home",
            "url":"/tasks"
        },
        "tasks": tasks,
        "categories": categories,
        "lables": lables
    }
    return render(request, "home.html", context)
