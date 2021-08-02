from django.contrib.auth.decorators import login_required
from rest_framework.response import Response

from todoapp.settings import LOGIN_REDIRECT_URL
from todolist import utils


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
    return send_response(request, tasks)


@login_required(login_url=LOGIN_REDIRECT_URL)
def get_tasks_filter_by_category(request, category_id: int):
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
    return send_response(request, tasks)


@login_required(login_url=LOGIN_REDIRECT_URL)
def get_tasks_filter_by_lable(request, lable_id: int):
    user_id = request.user.id
    from todolist.storages.storage_implementation \
        import StorageImplementation
    from todolist.presenters.presenter_implementation \
        import PresenterImplementation
    presenter = PresenterImplementation()
    storage = StorageImplementation()
    from todolist.interactors.get_tasks import GetTasks
    interactor = GetTasks(storage=storage, presenter=presenter)
    tasks = interactor.get_tasks_filter_by_lable_wrapper(
        user_id=user_id, lable_id=lable_id)
    return send_response(request, tasks)


def send_response(request, tasks):
    categories = utils.get_all_categories()
    lables = utils.get_all_lables()
    response = {
        "tasks": tasks,
        "categories": categories,
        "lables": lables
    }
    return Response(response)
