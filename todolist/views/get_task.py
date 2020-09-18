from django.shortcuts import render


def get_task(request, task_id):

    from todolist.storages.storage_implementation import StorageImplementation
    from todolist.presenters.presenter_implementation import PresenterImplementation
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    from todolist.interactors.get_task import GetTask
    interactor = GetTask(storage=storage, presenter=presenter)
    task_details = interactor.get_task_wrapper(task_id)
    return render(request, "home.html", {"task", task_details})