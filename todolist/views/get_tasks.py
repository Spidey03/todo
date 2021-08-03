from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todoapp.settings import LOGIN_REDIRECT_URL
from todolist import utils


@api_view(["GET"])
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
    response = interactor.get_tasks_filter_by_lable_wrapper(
        user_id=user_id, lable_id=lable_id)
    return send_response(request, response)


def send_response(request, response):
    categories = utils.get_all_categories()
    labels = utils.get_all_labels()
    response["response"]["categories"] = [category.__dict__ for category in categories]
    response["response"]["labels"] = [label.__dict__ for label in labels]

    return Response(response)
