from unittest.mock import create_autospec, Mock

import pytest

from todolist.tests.common_fixtures.reset_sequence import reset


class TestGetTodosInteractor:

    @pytest.fixture()
    def task_dtos(self):
        reset()
        from todolist.tests.common_fixtures.factories \
            import TaskDTOFactory
        task_dtos = TaskDTOFactory.create_batch(2)
        return task_dtos

    @pytest.fixture()
    def category_dtos(self):
        reset()
        from todolist.tests.common_fixtures.factories \
            import CategoryDTOFactory
        category_dtos = CategoryDTOFactory.create_batch(2)
        return category_dtos

    @pytest.fixture()
    def task_lable_dtos(self):
        reset()
        from todolist.tests.common_fixtures.factories \
            import TaskLableDTOFactory
        task_lable_dtos = TaskLableDTOFactory.create_batch(2)
        return task_lable_dtos

    @pytest.fixture()
    def presenter_mock(self):
        from todolist.interactors.presenters.presenter_interface \
            import PresenterInterface
        presenter_mock = create_autospec(PresenterInterface)
        return presenter_mock

    @pytest.fixture
    def storage_mock(self):
        from todolist.interactors.storages.stroage_interface \
            import StorageInterface
        storage_interface = create_autospec(StorageInterface)
        return storage_interface

    def test_get_todos(
            self, storage_mock, presenter_mock,
            task_dtos, category_dtos, task_lable_dtos):
        # Arrange
        from todolist.interactors.get_tasks import GetTasks
        interactor = GetTasks(storage=storage_mock, presenter=presenter_mock)
        storage_mock.get_tasks.return_value = task_dtos
        storage_mock.get_categories.return_value = category_dtos
        storage_mock.get_lables_for_tasks.return_value = task_lable_dtos
        presenter_mock.response_get_tasks.return_value = Mock()

        # Act
        interactor.get_tasks_wrapper()

        # Assert
        presenter_mock.response_get_tasks.assert_called_once()
