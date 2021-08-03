from todolist.exceptions.exceptions import InvalidCategoryException, InvalidLableException, \
    InvalidValueForTitleException, InvalidValueForContentException
from todolist.interactors.mixins.validation_mixin import ValidationMixin
from todolist.interactors.presenters.presenter_interface import PresenterInterface
from todolist.interactors.storages.stroage_interface import StorageInterface


class AddNewTask(ValidationMixin):
    def __init__(self,
                 storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def add_new_task_wrapper(
            self, title: str, content: str, category, label, date):
        try:
            self.add_new_task(title=title, content=content,
                              category=category, label=label, date=date)
            response = self.presenter.successfully_created_task()
        except InvalidValueForTitleException:
            response = self.presenter.raise_invalid_value_for_title()
        except InvalidValueForContentException:
            response = self.presenter.raise_invalid_value_for_content()
        except InvalidCategoryException:
            response = self.presenter.raise_invalid_category_exception()
        except InvalidLableException:
            response = self.presenter.raise_invalid_lable_exception()
        return response

    def add_new_task(self, title, content, category, label, date):
        self._validate_title(title=title)
        print(title, content, category, label, date)
        # self._validate_content(content=content)
        category_id = self._get_category_if_valid(category)
        lable_id = self._get_lable_if_valid(label)
        self.storage.add_new_task(title, content, category_id, lable_id,
                                  date=date)
