from dataclasses import dataclass
from typing import List


@dataclass
class TaskDTO:
    id: int
    title: str
    content: str
    category_id: int
    date: str
    editable: bool = False
    active: bool = False
    stage: bool = False


@dataclass
class CategoryDTO:
    id: int
    name: str


@dataclass
class TaskLableDTO:
    lable_name: str
    task_id: int


@dataclass
class TaskDetailsDTO:
    id: int
    title: str
    content: str
    date: str
    category: str
    task_lables: List[TaskLableDTO]

@dataclass
class UserDetailsDTO:
    user_id: int
    username: str
    email: str
    firstname: str
    lastname: str
    bio: str
    profile_pic: str