import datetime

import pytest

from todolist.storages.storage_implementation import StorageImplementation
from todolist.tests.common_fixtures.reset_sequence import reset
from todolist.tests.factory import CategoryFactory


class TestGetTodosStorage:

    @pytest.fixture()
    def categories(self):
        reset()
        categories = CategoryFactory.create_batch(2)
        return categories

    @pytest.fixture()
    def lables(self):
        reset()
        from todolist.tests.common_fixtures.factories \
            import LableFactory
        lables = LableFactory.create()

    @pytest.fixture()
    def tasks_dtos(self):
        reset()
        from todolist.tests.common_fixtures.factories \
            import TaskDTOFactory
        from todolist.tests.common_fixtures.factories import CategoryDTOFactory
        CategoryDTOFactory.create(id='Category0')
        expected_result = TaskDTOFactory.create_batch(
            4, category_id=2, date='2020-01-01')
        return expected_result

    @pytest.fixture()
    def tasks(self):
        reset()
        from todolist.tests.common_fixtures.factories \
            import TaskFactory
        categories = CategoryFactory.create_batch(2)
        tasks = TaskFactory.create_batch(
            4, date=datetime.date(2020, 1, 1),
            category=categories[0])
        return tasks

    @pytest.mark.django_db
    def test_get_tasks_when_no_tasks(self):
        # Arrange
        expected_result = []
        storage = StorageImplementation()

        # Act
        tasks = storage.get_tasks()

        # Assert
        assert tasks == expected_result

    @pytest.mark.django_db
    def test_get_tasks_when_tasks_exist(self, categories, tasks, tasks_dtos):
        # Arrange
        expected_result = tasks_dtos
        storage = StorageImplementation()

        # Act
        tasks = storage.get_tasks()

        # Assert
        assert tasks == expected_result

    @pytest.mark.django_db
    def get_categories_when_no_categories(self):
        pass
