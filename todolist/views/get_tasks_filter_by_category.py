from django.shortcuts import render


def get_task_filter_by_category(request, category_id: int):
    user_id = request.user.id
    from todolist.storages.storage_implementation \
        import StorageImplementation
    from todolist.presenters.presenter_implementation \
        import PresenterImplementation
    presenter = PresenterImplementation()
    storage = StorageImplementation()
    from todolist.interactors.get_tasks import GetTasks
    interactor = GetTasks(storage=storage, presenter=presenter)
    tasks = interactor.get_tasks_filter_by_category_wrapper(
        user_id=user_id, category_id=category_id)
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
        "tasks": tasks,
        "categories": categories,
        "lables": lables
    }
    return render(request, "home.html", context)
