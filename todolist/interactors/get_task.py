from todolist.interactors.presenters.presenter_interface \
    import PresenterInterface
from todolist.interactors.storages.stroage_interface \
    import StorageInterface


class GetTask:
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_task_wrapper(self, task_id: int, user_id: str):
        task_details_dto = self.get_task(task_id=task_id, user_id=user_id)
        response = self.presenter.resposne_get_task(task_details_dto[0])
        return response

    def get_task(self, task_id: int, user_id: str):
        task = self.storage.get_task(task_id=task_id, user_id=user_id)
        category_id = task.category_id
        category_dto = self.storage.get_category_with_id(category_id=category_id)
        lable_dtos = self.storage.get_lables_for_task(task_id=task_id)
        task_details_dto = self._convert_to_task_details_dtos(
            categories=[category_dto], tasks=[task], lables=lable_dtos)
        return task_details_dto

    def _convert_to_task_details_dtos(self, categories, lables, tasks):
        from todolist.interactors.storages.dtos \
            import TaskDetailsDTO
        task_details_dtos = []
        for task in tasks:
            category = self._get_category_for_task(
                categories=categories, category_id=task.category_id)
            task_lables = self._get_lables_for_task(
                lables=lables, task_id=task.id
            )
            task_details_dtos.append(
                TaskDetailsDTO(
                    id=task.id,
                    title=task.title,
                    content=task.content,
                    date=task.date,
                    category=category,
                    task_lables=task_lables
                )
            )
        return task_details_dtos

    def _get_category_for_task(self, categories, category_id):
        for category in categories:
            if category.id == category_id:
                return category.name

    def _get_lables_for_task(self, lables, task_id):
        task_lables = []
        for lable in lables:
            if lable.task_id == task_id:
                task_lables.append(lable)
        return task_lables
