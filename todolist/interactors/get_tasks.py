from dataclasses import dataclass

from todolist.interactors.presenters.presenter_interface import \
    PresenterInterface
from todolist.interactors.storages.stroage_interface import StorageInterface


class GetTasks:
    def __init__(
            self, presenter: PresenterInterface, storage: StorageInterface):
        self.storage = storage
        self.presenter = presenter

    def get_tasks_wrapper(self, user_id: int):
        task_details_dtos = self.get_tasks(user_id=user_id)
        response = self.presenter.response_get_tasks(task_details_dtos)
        return response

    def get_tasks_filter_by_category_wrapper(
            self, user_id: int, category_id: int):
        task_details_dtos = self.get_tasks_filter_by_category(
            user_id=user_id, category_id=category_id)
        response = self.presenter.response_get_tasks(task_details_dtos)
        return response

    def get_tasks_filter_by_lable_wrapper(self, user_id, lable_id: int):
        task_details_dtos = self.get_tasks_filter_by_lable(
            user_id=user_id, lable_id=lable_id)
        response = self.presenter.response_get_tasks(task_details_dtos)
        return response

    def get_tasks_filter_by_lable(self, user_id: int, lable_id: int):
        tasks = self.storage.get_tasks_filter_by_lable(
            user_id=user_id, lable_id=lable_id)
        task_ids = [task.id for task in tasks]
        category_ids = [task.category_id for task in tasks]
        categories = self.storage.get_categories(
            category_ids=category_ids)
        lables = self.storage.get_lables_for_tasks(task_ids=task_ids)
        task_details_dtos = self._convert_to_task_details_dtos(
            categories, lables, tasks)
        return task_details_dtos


    def get_tasks_filter_by_category(self, user_id: int, category_id: int):
        tasks = self.storage.get_tasks_filter_by_category(
            user_id=user_id, category_id=category_id)
        task_ids = [task.id for task in tasks]
        category_ids = [task.category_id for task in tasks]
        categories = self.storage.get_categories(
            category_ids=category_ids)
        lables = self.storage.get_lables_for_tasks(task_ids=task_ids)
        task_details_dtos = self._convert_to_task_details_dtos(
            categories, lables, tasks)
        return task_details_dtos

    def get_tasks(self, user_id: int):
        tasks = self.storage.get_tasks(user_id=user_id)
        task_ids = [task.id for task in tasks]
        category_ids = [task.category_id for task in tasks]
        categories = self.storage.get_categories(
            category_ids=category_ids)
        lables = self.storage.get_lables_for_tasks(task_ids=task_ids)
        task_details_dtos = self._convert_to_task_details_dtos(
            categories, lables, tasks)
        return task_details_dtos

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

