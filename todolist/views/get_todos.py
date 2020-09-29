from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from todoapp.settings import LOGIN_REDIRECT_URL


@login_required(login_url=LOGIN_REDIRECT_URL)
def get_todos(request):
    user_id  = request.user.id
    from todolist.storages.storage_implementation \
        import StorageImplementation
    from todolist.presenters.presenter_implementation \
        import PresenterImplementation
    presenter = PresenterImplementation()
    storage = StorageImplementation()
    from todolist.interactors.get_todos import GetTodos
    interactor = GetTodos(storage=storage, presenter=presenter)
    todos = interactor.get_todos_wrapper(user_id=user_id)
    from todolist.views.user_details import user_details
    # TODO: implement categories
    from todolist.models import Category
    categories = Category.objects.all()

    from todolist.models import Lable
    lables = Lable.objects.all()
    return render(request, "home1.html",
                  {"todos": todos, 'categories': categories, "lables": lables})

