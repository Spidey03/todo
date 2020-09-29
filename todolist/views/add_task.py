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
    return render(request, "add_task.html", {'categories': categories})
