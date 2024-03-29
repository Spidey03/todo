from typing import List

from todolist.interactors.dtos import CreateUserDTO
from todolist.interactors.storages.dtos import TaskDTO, CategoryDTO, \
    TaskLableDTO, UserDetailsDTO
from todolist.interactors.storages.stroage_interface import StorageInterface


class StorageImplementation(StorageInterface):

    def check_username_is_taken(self, username):
        from todolist.models import User
        from todolist.exceptions.exceptions import \
            UsernameAlreadyTakenException
        is_exist = User.objects.filter(username=username).exists()
        if is_exist:
            raise UsernameAlreadyTakenException()

    def check_email_register_already(self, email):
        from todolist.models import User
        from todolist.exceptions.exceptions import \
            UserAlreadyRegisteredWithThisEmailException
        is_exist = User.objects.filter(email=email).exists()
        if is_exist:
            raise UserAlreadyRegisteredWithThisEmailException()

    def create_user(self, user_dto: CreateUserDTO):
        from todolist.models import User
        user = User.objects.create(
            username=user_dto.username,
            email=user_dto.email,
            bio=user_dto.email,
            first_name=user_dto.first_name,
            last_name=user_dto.last_name,
            profile_pic=user_dto.profile_pic
        )
        user.set_password(user_dto.password1)
        user.save()

    def validate_username(self, username: str):
        from todolist.models import User
        print(User.objects.all())
        is_user_exist = User.objects.filter(username=username).exists()
        if not is_user_exist:
            from todolist.exceptions.exceptions import \
                UserDoesNotExistException
            raise UserDoesNotExistException()

    def validate_password(self, username: str, password: str):
        from todolist.models import User
        from todolist.exceptions.exceptions import \
            UserDoesNotExistException
        from todolist.exceptions.exceptions import InvalidPasswordException
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise UserDoesNotExistException()

        if not user.check_password(password):
            raise InvalidPasswordException()
        return user.id

    def add_category(self, name: str):
        from todolist.models import Category
        Category.objects.create(name=name)

    def add_lable(self, name: str):
        from todolist.models import Label
        Label.objects.create(name=name)

    def check_is_lable_valid(self, name: str):
        from todolist.models import Label
        is_exist = Label.objects.filter(name=name).exists()
        return is_exist

    def get_category(self, name: str):
        from todolist.models import Category
        category = Category.objects.get(name=name)
        return category.id

    def get_all_categories(self):
        from todolist.models import Category
        categories = Category.objects.values('id', 'name')
        category_dtos = self._convert_to_category_dtos(categories)
        return category_dtos

    def check_is_category_valid(self, name: str):
        from todolist.models import Category
        is_exist = Category.objects.filter(name=name).exists()
        return is_exist

    def get_lable(self, name):
        from todolist.models import Label
        lable = Label.objects.get(name=name)
        return lable.id

    def add_new_task(self, title, content, category, lable, date):
        from todolist.models import UserTask
        print(title, content, category, lable, date)
        id = UserTask.objects.create(title=title, content=content,
                                category_id=category, date=date)
        print(id)

    def update_task(self, task_id, title, content, category_id, lables, date):
        from todolist.models import UserTask
        UserTask.objects.filter(id=task_id).update(
            title=title,
            content=content,
            category_id=category_id,
            date=date
        )

    def get_tasks(self, user_id: int) -> List[TaskDTO]:
        from todolist.models import UserTask
        # TODO: Filter with user
        tasks = UserTask.objects.all()
        task_dtos = self._convert_to_task_dtos(tasks)
        return task_dtos

    def get_tasks_filter_by_category(self, user_id, category_id):
        from todolist.models import UserTask
        tasks = UserTask.objects.filter(
            user_id=user_id, category_id=category_id)
        task_dtos = self._convert_to_task_dtos(tasks)
        return task_dtos

    def get_tasks_filter_by_lable(self, user_id, lable_id):
        from todolist.models import TaskLable
        from todolist.models import UserTask
        task_ids = TaskLable.objects.filter(lable_id=lable_id).values_list(
            'task_id')
        tasks = UserTask.objects.filter(
            user_id=user_id, id__in=task_ids)
        task_dtos = self._convert_to_task_dtos(tasks)
        return task_dtos

    def _convert_to_task_dtos(self, tasks):
        task_dtos = []
        for task in tasks:
            task_dtos.append(
                self._convert_to_task_dto(task)
            )
        return task_dtos

    def _convert_to_task_dto(self, task) -> TaskDTO:
        return TaskDTO(
            id=task.id,
            title=task.title,
            content=task.content,
            category_id=task.category_id,
            date=str(task.date),
            editable=task.editable,
            active=task.active,
            stage=task.stage
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
        from todolist.models import TaskLable, Label
        task_lables = TaskLable.objects.filter(task_id__in=task_ids)
        lable_ids = [task_lable.lable_id for task_lable in task_lables]
        lables = Label.objects.filter(id__in=lable_ids)
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

    def get_task(self, task_id: int, user_id: str):
        from todolist.models import UserTask
        task = UserTask.objects.get(id=task_id, user_id=user_id)
        return self._convert_to_task_dto(task=task)

    def get_category_with_id(self, category_id: int):
        from todolist.models import Category
        category = Category.objects.get(id=category_id)
        category_dto = CategoryDTO(id=category.id, name=category.name)
        return category_dto

    def get_lables_for_task(self, task_id: int):
        from todolist.models import TaskLable
        lable_ids = TaskLable.objects.filter(task_id=task_id)
        from todolist.models import Label
        lables = Label.objects.filter(id__in=lable_ids)
        task_lable_dtos = []
        for lable in lables:
            task_lable_dtos.append(
                TaskLableDTO(
                    task_id=task_id,
                    lable_name=lable.name
                )
            )
        return task_lable_dtos

    def get_profile_details(self, user_id):
        from todolist.models import User
        user = User.objects.get(id=user_id)
        user_details_dto = UserDetailsDTO(
            user_id=user.id,
            username=user.username,
            email=user.email,
            firstname=user.first_name,
            lastname=user.last_name,
            bio=user.bio,
            profile_pic=user.profile_pic
        )
        return user_details_dto

    def check_task_id_valid(self, task_id):
        from todolist.models import UserTask
        from todolist.exceptions.exceptions import TaskIsNotExistException
        is_exist = UserTask.objects.filter(id=task_id).exists()
        not_exist = not is_exist
        if not_exist:
            raise TaskIsNotExistException()
