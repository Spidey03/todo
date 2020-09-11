from unittest.mock import create_autospec

import pytest

from todolist.interactors.add_task import AddNewTask


class TestAddNewTaskInteractor:

    @pytest.fixture()
    def presenter_mock(self):
        from todolist.interactors.presenters.presenter_interface import PresenterInterface
        presenter_mock = create_autospec(PresenterInterface)
        return presenter_mock

    @pytest.fixture
    def storage_mock(self):
        from todolist.interactors.storages.stroage_interface import StorageInterface
        storage_interface = create_autospec(StorageInterface)
        return storage_interface

    def test_add_new_task_if_category_invalid_raise_exception(
            self, presenter_mock, storage_mock):
        # Arrange
        title = 'New Task'
        content = 'create a task'
        category = 'invalid'
        lable = 'lable'
        due_date = '25-02-2000'
        interactor = AddNewTask(
            presenter=presenter_mock, storage=storage_mock)
        storage_mock.check_is_category_valid.return_value = False

        # Act
        interactor.add_new_task_wrapper(
            title=title, content=content, category=category, lable=lable,
            due_date=due_date)

        # Assert
        presenter_mock.raise_invalid_category_exception.assert_called_once()

    def test_add_new_task_if_lable_invalid_raise_exception(
            self, presenter_mock, storage_mock):
        # Arrange
        title = 'New Task'
        content = 'create a task'
        category = 'Shopping'
        lable = 'invalid lable'
        due_date = '25-02-2000'
        interactor = AddNewTask(
            presenter=presenter_mock, storage=storage_mock)
        storage_mock.check_is_category_valid.return_value = True
        storage_mock.check_is_lable_valid.return_value = False

        # Act
        interactor.add_new_task_wrapper(
            title=title, content=content, category=category, lable=lable,
            due_date=due_date)

        # Assert
        presenter_mock.raise_invalid_lable_exception.assert_called_once()

    def test_add_new_task_successfully_create_task(
            self, presenter_mock, storage_mock):
        # Arrange
        title = 'New Task'
        content = 'create a task'
        category = 'Shopping'
        lable = 'Amazon'
        due_date = '25-02-2000'
        interactor = AddNewTask(
            presenter=presenter_mock, storage=storage_mock)
        storage_mock.check_is_category_valid.return_value = True
        storage_mock.check_is_lable_valid.return_value = True

        # Act
        interactor.add_new_task_wrapper(
            title=title, content=content, category=category, lable=lable,
            due_date=due_date)

        # Asserts
        presenter_mock.successfully_created_task.assert_called_once()
