from dataclasses import dataclass


@dataclass
class CreateUserDTO:
    username: str
    first_name: str
    last_name: str
    email: str
    bio: str
    profile_pic: str
    password1: str
    password2: str