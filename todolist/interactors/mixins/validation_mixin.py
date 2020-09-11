


class ValidationMixin:
    def validate_name(self, name: str):
        from todolist.exceptions.exceptions import InvalidNameException
        valid = bool(name) and type(name) == str
        not_valid = not valid
        if not_valid:
            raise InvalidNameException
