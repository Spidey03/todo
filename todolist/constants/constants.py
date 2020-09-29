import enum

PROFILE_PIC = "static/images/user.jpg"


class StatusCode(enum.Enum):
    BadRequest = 400
    NotFound = 404
    Forbidden = 403
    Success = 200
    Created_Success = 201
