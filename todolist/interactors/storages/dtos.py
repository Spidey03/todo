from dataclasses import dataclass
from typing import List


@dataclass
class TaskDTO:
    id: int
    title: str
    content: str
    category_id: int
    date: str


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
