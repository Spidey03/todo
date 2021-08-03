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

    def _get_lable_if_valid(self, lable):
        from todolist.exceptions.exceptions import \
            InvalidLableException
        if lable:
            valid = self.storage.check_is_lable_valid(name=lable)
            if not valid:
                # TODO: raise error
                return  None
            return self.storage.get_lable(name=lable)

    def _get_category_if_valid(self, category):
        from todolist.exceptions.exceptions import \
            InvalidCategoryException
        if category:
            valid = self.storage.check_is_category_valid(name=category)
            if not valid:
                # TODO: raise error
                return None
            return self.storage.get_category(name=category)

    def _validate_title(self, title):
        from todolist.exceptions.exceptions import \
            InvalidValueForTitleException
        if type(title) != str or title == '':
            raise InvalidValueForTitleException()

    def _validate_content(self, content):
        from todolist.exceptions.exceptions import \
            InvalidValueForContentException
        if type(content) != str or content == '':
            raise InvalidValueForContentException()