from todolist.exceptions.exceptions import UserNameIsEmptyException, \
    EmailIsInvalidOrEmptyException, BioisEmptyException, \
    PasswordsShouldBeIdentical, PasswordDidnotMatchConstraintsException, \
    UsernameAlreadyTakenException, UserAlreadyRegisteredWithThisEmailException
from todolist.interactors.dtos import CreateUserDTO
from todolist.interactors.mixins.validation_mixin import ValidationMixin
from todolist.interactors.presenters.presenter_interface import \
    PresenterInterface
from todolist.interactors.storages.stroage_interface import StorageInterface


class Signup(ValidationMixin):
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def signup_wrapper(self, user_dto: CreateUserDTO,
                       presenter: PresenterInterface):
        try:
            self.signup(user_dto=user_dto)
            response = presenter.user_created_successfully()
        except UserNameIsEmptyException:
            response = presenter.raise_username_should_not_be_empty()
        except EmailIsInvalidOrEmptyException:
            response = presenter.raise_email_is_invalid()
        except BioisEmptyException:
            response = presenter.raise_bio_is_empty()
        except PasswordDidnotMatchConstraintsException:
            response = presenter.raise_password_not_match_to_constraints()
        except PasswordsShouldBeIdentical:
            response = presenter.raise_passwords_should_be_identical()
        except UsernameAlreadyTakenException:
            response = presenter.raise_username_already_taken()
        except UserAlreadyRegisteredWithThisEmailException:
            response = presenter.raise_user_already_register_with_this_email()
        return response

    def signup(self, user_dto: CreateUserDTO):
        self.validate_username(user_dto.username)
        self.validate_email(email=user_dto.email)
        self.validate_bio(bio=user_dto.bio)
        self.check_passwords_match(password1=user_dto.password1,
                                   password2=user_dto.password2)
        self.validate_password(password=user_dto.password1)
        self.storage.check_username_is_taken(user_dto.username)
        self.storage.check_email_register_already(user_dto.email)
        self.storage.create_user(user_dto)
