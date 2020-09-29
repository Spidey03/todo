from common.oauth2_storage import OAuth2SQLStorage
from todolist.exceptions.exceptions import UserDoesNotExistException, \
    InvalidPasswordException
from todolist.interactors.mixins.validation_mixin import ValidationMixin
from todolist.interactors.presenters.presenter_interface import \
    PresenterInterface
from todolist.interactors.storages.stroage_interface import StorageInterface


class Login(ValidationMixin):
    def __init__(self, storage: StorageInterface,
                 oauth_storage: OAuth2SQLStorage):
        self.storage = storage
        self.oauth_storage = oauth_storage

    def login_wrapper(self, username: str, password: str,
                      presenter: PresenterInterface):
        try:
            tokens_dto = self.login(username=username, password=password,
                       presenter=presenter)
            response = presenter.get_response_login_user(tokens_dto)
        except UserDoesNotExistException:
            response = presenter.raise_user_does_not_exist()
        except InvalidPasswordException:
            response = presenter.raise_password_is_incorrect()
        return response

    def login(self, username: str, password: str,
              presenter: PresenterInterface):
        self.storage.validate_username(username=username)
        user_id = self.storage.validate_password(username=username,
                                                 password=password)

        from common.oauth_user_auth_tokens_service \
            import OAuthUserAuthTokensService

        service = OAuthUserAuthTokensService(self.oauth_storage)

        tokens_dto = service.create_user_auth_tokens(user_id)

        return tokens_dto
