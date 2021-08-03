from rest_framework.decorators import api_view
from rest_framework.response import Response

from todolist import utils


@api_view(["GET"])
def get_task(request, task_id):
    user_id = request.user.id
    from todolist.storages.storage_implementation import StorageImplementation
    from todolist.presenters.presenter_implementation import PresenterImplementation
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    from todolist.interactors.get_task import GetTask
    interactor = GetTask(storage=storage, presenter=presenter)
    task_details = interactor.get_task_wrapper(task_id=task_id, user_id=user_id)
    categories = utils.get_all_categories()
    lables = utils.get_all_labels()
    response = {
        "task": task_details,
        "categories": categories,
        "lables": lables
    }
    return Response(response)