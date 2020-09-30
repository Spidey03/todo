from todolist.interactors.presenters.presenter_interface import \
    PresenterInterface
from todolist.interactors.storages.stroage_interface import StorageInterface


class GetProfile:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_profile_details_wrapper(
            self, user_id: int, presenter: PresenterInterface):
        user_details_dto = self.get_profile_details(user_id=user_id)
        response = presenter.response_get_profile(user_details_dto)
        return response

    def get_profile_details(self, user_id: int):
        user_details_dto = self.storage.get_profile_details(user_id=user_id)
        return user_details_dto