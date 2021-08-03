from todolist.exceptions.exceptions import InvalidValueForTitleException, \
    InvalidValueForContentException, InvalidCategoryException, \
    InvalidLableException, TaskIsNotExistException
from todolist.interactors.dtos import TaskDetailsDTO
from todolist.interactors.mixins.validation_mixin import ValidationMixin
from todolist.interactors.presenters.presenter_interface import \
    PresenterInterface
from todolist.interactors.storages.stroage_interface import StorageInterface


class UpdateTask(ValidationMixin):

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_task_wrapper(
            self, task_details_dto: TaskDetailsDTO,
            presenter: PresenterInterface):
        try:
            self.update_task(task_details_dto)
            response = presenter.successfully_created_task()
        except InvalidValueForTitleException:
            response = presenter.raise_invalid_value_for_title()
        except InvalidValueForContentException:
            response = presenter.raise_invalid_value_for_content()
        except InvalidCategoryException:
            response = presenter.raise_invalid_category_exception()
        except InvalidLableException:
            response = presenter.raise_invalid_lable_exception()
        except TaskIsNotExistException:
            response = presenter.raise_task_not_found_exception()
        return response

    def update_task(self, task_details_dto):
        self._validate_title(title=task_details_dto.title)
        # self._validate_content(content=task_details_dto.content)
        category_id = self._get_category_if_valid(task_details_dto.category)

        lable_id = self._get_lable_if_valid(task_details_dto.lables)
        self.storage.check_task_id_valid(task_details_dto.task_id)
        self.storage.update_task(
            task_id=task_details_dto.task_id,
            title=task_details_dto.title,
            content=task_details_dto.content,
            category_id=category_id,
            lables=[lable_id],
            date=task_details_dto.date
        )
