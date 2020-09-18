from typing import List

from todolist.interactors.storages.dtos import TaskDTO, CategoryDTO, TaskLableDTO
from todolist.interactors.storages.stroage_interface import StorageInterface


class StorageImplementation(StorageInterface):

    def add_category(self, name: str):
        from todolist.models import Category
        Category.objects.create(name=name)

    def add_lable(self, name: str):
        from todolist.models import Lable
        Lable.objects.create(name=name)

    def check_is_lable_valid(self, name: str):
        from todolist.models import Lable
        is_exist = Lable.objects.filter(name=name).exists()
        return is_exist

    def get_category(self, name: str):
        from todolist.models import Category
        category = Category.objects.get(name=name)
        return category.id

    def check_is_category_valid(self, name: str):
        from todolist.models import Category
        is_exist = Category.objects.filter(name=name).exists()
        return is_exist

    def get_lable(self, name):
        from todolist.models import Lable
        lable = Lable.objects.get(name=name)
        return lable.id

    def add_new_task(self, title, content, category, lable, date):
        from todolist.models import Task
        Task.objects.create(title=title, content=content,
                            category_id=category, date=date)

    def get_tasks(self) -> List[TaskDTO]:
        from todolist.models import Task
        tasks = Task.objects.all()
        task_dtos = self._convert_to_task_dtos(tasks)
        return task_dtos

    def _convert_to_task_dtos(self, tasks):
        task_dtos = []
        for task in tasks:
            task_dtos.append(
                self._convert_to_task_dto(task)
            )
        return task_dtos

    def _convert_to_task_dto(self, task):
        return TaskDTO(
            id=task.id,
            title=task.title,
            content=task.content,
            category_id=task.category_id,
            date=str(task.date)
        )

    def get_categories(self, category_ids: List[int]) -> List[CategoryDTO]:
        from todolist.models import Category
        categories = Category.objects.filter(
            id__in=category_ids).values('id', 'name')
        category_dtos = self._convert_to_category_dtos(categories)
        return category_dtos

    def _convert_to_category_dtos(self, categories) -> List[CategoryDTO]:
        category_dtos = []
        for category in categories:
            category_dtos.append(
                CategoryDTO(
                    id=category['id'],
                    name=category['name']
                )
            )
        return category_dtos

    def get_lables_for_tasks(self, task_ids: List[int]) -> List[TaskLableDTO]:
        from todolist.models import TaskLable, Lable
        task_lables = TaskLable.objects.filter(task_id__in=task_ids)
        lable_ids = [task_lable.lable_id for task_lable in task_lables]
        lables = Lable.objects.filter(id__in=lable_ids)
        lable_dtos = []
        for task_lable in task_lables:
            for lable in lables:
                if lable.id == task_lable.lable_id:
                    lable_dtos.append(
                        TaskLableDTO(
                            task_id=task_lable.task_id,
                            lable_name=lable.name
                        )
                    )
        return lable_dtos

    def get_all_categories(self):
        from todolist.models import Category
        categories = Category.objects.values()
        return self._convert_to_category_dtos(
            categories=categories)

    def get_task(self, task_id: int):
        from todolist.models import Task
        task = Task.objects.get(id=task_id)
        return self._convert_to_task_dto(task=task)

    def get_category_with_id(self, category_id: int):
        from todolist.models import Category
        category = Category.objects.get(id=category_id)
        category_dto = CategoryDTO(id=category.id, name=category.name)
        return category_dto

    def get_lables_for_task(self, task_id: int):
        from todolist.models import TaskLable
        lable_ids = TaskLable.objects.filter(task_id=task_id)
        from todolist.models import Lable
        lables = Lable.objects.filter(id__in=lable_ids)
        task_lable_dtos = []
        for lable in lables:
            task_lable_dtos.append(
                TaskLableDTO(
                    task_id=task_id,
                    lable_name=lable.name
                )
            )
        return task_lable_dtos

