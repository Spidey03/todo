from unittest.mock import create_autospec, Mock

import pytest

from todolist.interactors.add_lable import AddNewLable


class TestAddNewCategory:

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

    def test_add_new_category_if_name_invalid_raises_exception(
            self, presenter_mock, storage_mock):
        # Arrange
        interactor = AddNewLable(
            storage=storage_mock, presenter=presenter_mock)
        name = ''
        presenter_mock.return_value = Mock()

        # Act
        interactor.add_lable_wrapper(name=name)

        # Assert
        presenter_mock.raise_invalid_lable_name_exception.assert_called_once()

    def test_add_new_category_creates_category_successfully(
            self, presenter_mock, storage_mock):
        # Arrange
        interactor = AddNewLable(
            storage=storage_mock, presenter=presenter_mock)
        name = 'New_Lable'
        presenter_mock.return_value = Mock()

        # Act
        interactor.add_lable_wrapper(name=name)

        # Assert
        presenter_mock.successfully_created_lable.assert_called_once()
