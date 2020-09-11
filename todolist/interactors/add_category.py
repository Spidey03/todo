from todolist.exceptions.exceptions import InvalidNameException
from todolist.interactors.mixins.validation_mixin import ValidationMixin
from todolist.interactors.presenters.presenter_interface import PresenterInterface
from todolist.interactors.storages.stroage_interface import StorageInterface


class AddNewCategory(ValidationMixin):
    def __init__(
            self, storage: StorageInterface,
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def add_category_wrapper(self, name: str):
        try:
            self.add_category(name=name)
            response = self.presenter.successfully_created_category()
        except InvalidNameException:
            response = self.presenter.raise_invalid_category_name_exception()
        return response

    def add_category(self, name: str):
        self.validate_name(name=name)
        self.storage.add_category(name=name)


