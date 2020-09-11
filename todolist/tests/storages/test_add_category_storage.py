import pytest

from todolist.storages.storage_implementation import StorageImplementation


class TestAddCategoryStorage:

    @pytest.mark.django_db
    def test_add_category(self):
        # Arrange
        name = 'New Category'
        storage = StorageImplementation()

        # Act
        storage.add_category(name=name)

        # Assert
        from todolist.models import Category
        assert Category.objects.all().count() == 1