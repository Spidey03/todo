class ValidationMixin:
    @staticmethod
    def validate_name(name: str):
        from todolist.exceptions.exceptions import InvalidNameException
        valid = bool(name) and type(name) == str
        not_valid = not valid
        if not_valid:
            raise InvalidNameException

    @staticmethod
    def validate_username(value):
        from todolist.exceptions.exceptions import UserNameIsEmptyException
        valid = bool(value) and type(value) == str
        not_valid = not valid
        if not_valid:
            raise UserNameIsEmptyException

    @staticmethod
    def validate_email(email):
        from todolist.exceptions.exceptions import \
            EmailIsInvalidOrEmptyException
        valid = bool(email) and type(email) == str
        not_valid = not valid
        if not_valid:
            raise EmailIsInvalidOrEmptyException

    @staticmethod
    def validate_bio(bio):
        from todolist.exceptions.exceptions import BioisEmptyException
        valid = bool(bio) and type(bio) == str
        not_valid = not valid
        if not_valid:
            raise BioisEmptyException

    @staticmethod
    def validate_password(password):
        from todolist.exceptions.exceptions import \
            PasswordDidnotMatchConstraintsException
        valid = bool(password) and type(password) == str
        not_valid = not valid
        if not_valid:
            raise PasswordDidnotMatchConstraintsException()

    @staticmethod
    def check_passwords_match(password1, password2):
        from todolist.exceptions.exceptions import \
            PasswordsShouldBeIdentical
        if not password1 == password2:
            raise PasswordsShouldBeIdentical()
