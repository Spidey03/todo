from todolist.interactors.presenters.presenter_interface \
    import PresenterInterface
from todolist.interactors.storages.stroage_interface \
    import StorageInterface


class GetTask:
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_task_wrapper(self, task_id: int):
        try:
            task_details_dto = self.get_task(task_id=task_id)
            response = self.presenter.resposne_get_task(task_details_dto)
            return response
        except:
            pass

    def get_task(self, task_id: int):
        task = self.storage.get_task(task_id=task_id)
        category_id = task.category_id
        category_dto = self.storage.get_category_with_id(category_id=category_id)
        lable_dtos = self.storage.get_lables_for_task(task_id=task_id)
        task_details_dto = self._convert_to_task_details_dto(
            category_dto, task, lable_dtos, task_id)
        return task_details_dto

    def _convert_to_task_details_dto(self, category_dto, task, lables, task_id):
        from todolist.interactors.storages.dtos import TaskDetailsDTO
        return TaskDetailsDTO(
            id=task_id,
            title=task.title,
            content=task.content,
            date=task.date,
            category=category_dto.name,
            task_lables=[lable.name for lable in lables]
        )
