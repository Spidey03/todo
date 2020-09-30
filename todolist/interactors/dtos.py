from dataclasses import dataclass
from typing import List


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


@dataclass
class TaskDetailsDTO:
    user_id: int
    task_id: int
    title: str
    content: str
    category: str
    date: str
    lables: List[str]