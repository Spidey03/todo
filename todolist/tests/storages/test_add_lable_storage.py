import pytest

from todolist.storages.storage_implementation import StorageImplementation


class TestAddCategoryStorage:

    @pytest.mark.django_db
    def test_add_category(self):
        # Arrange
        name = 'New Lable'
        storage = StorageImplementation()

        # Act
        storage.add_lable(name=name)

        # Assert
        from todolist.models import Lable
        assert Lable.objects.all().count() == 1