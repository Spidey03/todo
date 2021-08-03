from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def add_task(request):
    details = request.data
    title = details.get('title')
    content = details.get('content', "")
    date = details.get('date', str(datetime.today().date()))
    category = details.get('category', None)
    label = details.get('label', 'Home')

    print(date)

    from todolist.presenters.presenter_implementation import \
        PresenterImplementation
    from todolist.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    from todolist.interactors.add_task import AddNewTask
    interactor = AddNewTask(storage=storage, presenter=presenter)

    response = interactor.add_new_task_wrapper(
        title=title, content=content, date=date, category=category,
        label=label
    )

    return Response(response)
