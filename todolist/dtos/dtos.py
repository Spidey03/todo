import dataclasses


@dataclasses.dataclass
class UserDTO:
    id: int
    username: str
    email: str
    bio: str
    firstname: str
    lastname: str
    profile_pic: str


@dataclasses.dataclass
class LableDTO:
    id: int
    name: str


@dataclasses.dataclass
class CategoryDTO:
    id: int
    name: str
