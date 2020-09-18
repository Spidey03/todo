from todolist.interactors.presenters.presenter_interface import PresenterInterface
from todolist.interactors.storages.stroage_interface import StorageInterface


class GetCategories:
    def __init__(
            self, storage: StorageInterface,
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_categories_wrapper(self):
        category_dtos = self.get_categories()
        response = self.presenter.response_get_categories(category_dtos)
        return response

    def get_categories(self):
        categories = self.storage.get_all_categories()
        return categories