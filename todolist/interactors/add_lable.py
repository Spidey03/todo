from todolist.exceptions.exceptions import InvalidNameException
from todolist.interactors.mixins.validation_mixin import ValidationMixin
from todolist.interactors.presenters.presenter_interface import PresenterInterface
from todolist.interactors.storages.stroage_interface import StorageInterface


class AddNewLable(ValidationMixin):
    def __init__(
            self, storage: StorageInterface,
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def add_lable_wrapper(self, name: str):
        try:
            self.add_lable(name=name)
            response = self.presenter.successfully_created_lable()
        except InvalidNameException:
            response = self.presenter.raise_invalid_lable_name_exception()
        return response

    def add_lable(self, name: str):
        self.validate_name(name=name)
        self.storage.add_lable(name=name)


