from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from todoapp.settings import LOGIN_REDIRECT_URL


@login_required(login_url=LOGIN_REDIRECT_URL)
def add_task(request):
    from todolist.storages.storage_implementation import StorageImplementation
    storage = StorageImplementation()
    from todolist.presenters.presenter_implementation import \
        PresenterImplementation
    presenter = PresenterImplementation()
    from todolist.interactors.get_categories import GetCategories
    interactor = GetCategories(storage=storage, presenter=presenter)
    categories = interactor.get_categories_wrapper()
    # TODO: IMPLEMENT GET LABLE
    from todolist.models import Lable
    # TODO: IMPLEMENT GET USER
    from todolist.models import User
    user = User.objects.get(id=request.get.id)
    lables = Lable.objects.all()
    context = {
        "title": {
            "name": "Home",
            "url": "/tasks"
        },
        "user": user,
        "categories": categories,
        "lables": lables
    }
    return render(request, "add_task.html", context)

