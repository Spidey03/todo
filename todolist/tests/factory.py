import factory

from todolist import models


class CategoryFactory(factory.Factory):
    class Meta:
        model = models.Category

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f'category {n}')
