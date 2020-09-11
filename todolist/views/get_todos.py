from django.shortcuts import render

from todolist.models import Task, Category


def get_todos(request):
    from todolist.storages.storage_implementation \
        import StorageImplementation
    from todolist.presenters.presenter_implementation \
        import PresenterImplementation
    presenter = PresenterImplementation()
    storage = StorageImplementation()
    from todolist.interactors.get_todos import GetTodos
    interactor = GetTodos(storage=storage, presenter=presenter)
    todos = interactor.get_todos_wrapper()
    return render(request, "home.html",
                  {"todos": todos})

