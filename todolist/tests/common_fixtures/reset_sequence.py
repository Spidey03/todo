from todolist.tests.common_fixtures.factories import TaskDTOFactory, CategoryDTOFactory, TaskLableDTOFactory, \
    TaskDetailsDTOFactory, TaskFactory, LableFactory, CategoryFactory, TaskLableFactory


def reset():
    reset_dto_factories()
    reset_model_factories()


def reset_model_factories():
    CategoryFactory.reset_sequence(0)
    TaskFactory.reset_sequence(0)
    LableFactory.reset_sequence(0)
    TaskLableFactory.reset_sequence(0)


def reset_dto_factories():
    TaskDTOFactory.reset_sequence(0)
    CategoryDTOFactory.reset_sequence(0)
    TaskLableDTOFactory.reset_sequence(0)
    TaskDetailsDTOFactory.reset_sequence(0)
