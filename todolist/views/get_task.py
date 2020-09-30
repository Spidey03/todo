from django.shortcuts import render


def get_task(request, task_id):
    user_id = request.user.id
    from todolist.storages.storage_implementation import StorageImplementation
    from todolist.presenters.presenter_implementation import PresenterImplementation
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    from todolist.interactors.get_task import GetTask
    interactor = GetTask(storage=storage, presenter=presenter)
    task_details = interactor.get_task_wrapper(task_id)
    categories = storage.get_all_categories()
    # TODO: IMPLEMENT GET USER
    from todolist.models import User
    user = User.objects.get(id=user_id)
    # TODO: IMPLEMENT GET CATEGORY
    categories = storage.get_all_categories()
    # TODO: IMPLEMENT GET LABLE
    from todolist.models import Lable
    lables = Lable.objects.all()
    context = {
        "title": {
            "name": "Home",
            "url": "/tasks"
        },
        "user": user,
        "task": task_details,
        "categories": categories,
        "lables": lables
    }
    return render(request, "task.html", context)