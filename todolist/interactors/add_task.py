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
            self, title: str, content: str, category, lable, date):
        try:
            self.add_new_task(title=title, content=content,
                              category=category, lable=lable, date=date)
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

    def add_new_task(self, title, content, category, lable, date):
        self._validate_title(title=title)
        self._validate_content(content=content)
        category_id = self._get_category_if_valid(category)
        lable_id = self._get_lable_if_valid(lable)
        self.storage.add_new_task(title, content, category_id, lable_id,
                                  date=date)

    def _get_lable_if_valid(self, lable):
        if lable:
            valid = self.storage.check_is_lable_valid(name=lable)
            if not valid:
                raise InvalidLableException()
            return self.storage.get_lable(name=lable)

    def _get_category_if_valid(self, category):
        if category:
            valid = self.storage.check_is_category_valid(name=category)
            if not valid:
                raise InvalidCategoryException()
            return self.storage.get_category(name=category)

    def _validate_title(self, title):
        if type(title) != str or title == '':
            raise InvalidValueForTitleException()

    def _validate_content(self, content):
        if type(content) != str or content == '':
            raise InvalidValueForContentException()
