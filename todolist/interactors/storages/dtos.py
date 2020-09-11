from dataclasses import dataclass


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