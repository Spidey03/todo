import abc
from typing import List

from todolist.interactors.storages.dtos import TaskDTO, CategoryDTO, TaskLableDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def add_category(self, name: str):
        pass

    @abc.abstractmethod
    def add_lable(self, name: str):
        pass

    @abc.abstractmethod
    def check_is_lable_valid(self, name: str):
        pass

    @abc.abstractmethod
    def get_category(self, name: str):
        pass

    @abc.abstractmethod
    def check_is_category_valid(self, name: str):
        pass

    @abc.abstractmethod
    def get_lable(self, name):
        pass

    @abc.abstractmethod
    def add_new_task(self, title, content, category, lable, date):
        pass

    @abc.abstractmethod
    def get_tasks(self) -> List[TaskDTO]:
        pass

    @abc.abstractmethod
    def get_categories(self, category_ids: List[int]) -> List[CategoryDTO]:
        pass

    @abc.abstractmethod
    def get_lables_for_tasks(self, task_ids: List[int]) -> List[TaskLableDTO]:
        pass

    @abc.abstractmethod
    def get_all_categories(self):
        pass

    @abc.abstractmethod
    def get_task(self, task_id: int):
        pass

    @abc.abstractmethod
    def get_category_with_id(self, category_id: int):
        pass

    @abc.abstractmethod
    def get_lables_for_task(self, task_id: int):
        pass
