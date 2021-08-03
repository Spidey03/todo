from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def update_task(request, task_id: int):
    user_id = request.user.id
    if request.method == 'POST':
        details = request.data
        title = details['title']
        content = details.get('content', '')
        date = details.get('date', str(datetime.today().date()))
        category = details.get('category', None)
        label = details.get('label', 'Home')

        task_details_dto = get_task_details_dto(
            category, content, date, task_id, title, user_id)
        from todolist.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        from todolist.presenters.presenter_implementation import \
            PresenterImplementation
        presenter = PresenterImplementation()
        from todolist.interactors.update_task import UpdateTask
        interactor = UpdateTask(storage=storage)
        response = interactor.update_task_wrapper(
            task_details_dto=task_details_dto, presenter=presenter)
        print(response)
        return Response(response)


def get_task_details_dto(category, content, date, task_id, title, user_id):
    from todolist.interactors.dtos import TaskDetailsDTO
    task_details_dto = TaskDetailsDTO(
        user_id=user_id,
        task_id=task_id,
        title=title,
        content=content,
        category=category,
        date=date,
        lables=['Home']
    )
    return task_details_dto

