import datetime

import factory
from factory import fuzzy

from todolist import models
from todolist.interactors.storages.dtos import TaskDTO, CategoryDTO, TaskLableDTO, TaskDetailsDTO


class TaskDTOFactory(factory.Factory):
    class Meta:
        model = TaskDTO

    id = factory.Sequence(lambda n: n)
    title = factory.Sequence(lambda n: "Title %03d" % n)
    content = factory.Sequence(lambda n: "Content %03d" % n)
    category_id = factory.Sequence(lambda n: n)
    date = fuzzy.FuzzyDate(datetime.date(2020, 1, 1))


class CategoryDTOFactory(factory.Factory):
    class Meta:
        model = CategoryDTO

    id = factory.Sequence(lambda n: "Category %d" % n)
    name = factory.Sequence(lambda n: "Category %03d" % n)


class TaskLableDTOFactory(factory.Factory):
    class Meta:
        model = TaskLableDTO

    lable_name = factory.Sequence(lambda n: "Lable %d" % n)
    task_id = factory.Sequence(lambda n: n)


class TaskDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskDetailsDTO

    id = factory.Sequence(lambda n: n)
    title = factory.Sequence(lambda n: "Title %03d" % n)
    content = factory.Sequence(lambda n: "Content %03d" % n)
    category = factory.Sequence(lambda n: "Category %d" % n)
    date = fuzzy.FuzzyDate(datetime.date(2020, 1, 1))
    task_lables = []

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    id = factory.Sequence(lambda n: "Category %d" % n)
    name = factory.Sequence(lambda n: "Category %03d" % n)

class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UserTask

    id = factory.Sequence(lambda n: n)
    title = factory.Sequence(lambda n: "Title %03d" % n)
    content = factory.Sequence(lambda n: "Content %03d" % n)
    category = factory.Iterator(models.Category.objects.all())
    date = fuzzy.FuzzyDate(datetime.date(2020, 1, 1))


class LableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Lable

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: "Lable %03d" % n)


class TaskLableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.TaskLable

    id = factory.Sequence(lambda n: n)
    lable = factory.SubFactory(LableFactory)
    task = factory.SubFactory(TaskFactory)



