class UserNameIsEmptyException(Exception):
    pass


class EmailIsInvalidOrEmptyException(Exception):
    pass


class BioisEmptyException(Exception):
    pass


class PasswordDidnotMatchConstraintsException(Exception):
    pass


class PasswordsShouldBeIdentical(Exception):
    pass


class UserDoesNotExistException(Exception):
    pass


class InvalidPasswordException(Exception):
    pass


class UsernameAlreadyTakenException(Exception):
    pass


class UserAlreadyRegisteredWithThisEmailException(Exception):
    pass


class InvalidNameException(Exception):
    pass


class InvalidLableException(Exception):
    pass


class InvalidCategoryException(Exception):
    pass


class InvalidValueForTitleException(Exception):
    pass


class InvalidValueForContentException(Exception):
    pass
