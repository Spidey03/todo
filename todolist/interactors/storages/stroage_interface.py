import abc
from typing import List

from todolist.interactors.dtos import CreateUserDTO
from todolist.interactors.storages.dtos import TaskDTO, CategoryDTO, \
    TaskLableDTO


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
    def update_task(self, task_id, title, content, category_id, lables, date):
        pass

    @abc.abstractmethod
    def get_tasks(self, user_id: int) -> List[TaskDTO]:
        pass

    @abc.abstractmethod
    def get_tasks_filter_by_category(self, user_id, category_id):
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
    def get_task(self, task_id: int, user_id: str):
        pass

    @abc.abstractmethod
    def get_category_with_id(self, category_id: int):
        pass

    @abc.abstractmethod
    def get_lables_for_task(self, task_id: int):
        pass

    @abc.abstractmethod
    def validate_username(self, username: str):
        pass

    @abc.abstractmethod
    def validate_password(self, username: str, password: str):
        pass

    @abc.abstractmethod
    def create_user(self, user_dto: CreateUserDTO):
        pass

    @abc.abstractmethod
    def check_username_is_taken(self, username):
        pass

    @abc.abstractmethod
    def check_email_register_already(self, email):
        pass

    @abc.abstractmethod
    def get_tasks_filter_by_lable(self, user_id, lable_id):
        pass

    @abc.abstractmethod
    def get_profile_details(self, user_id):
        pass

    @abc.abstractmethod
    def check_task_id_valid(self, task_id):
        pass
    