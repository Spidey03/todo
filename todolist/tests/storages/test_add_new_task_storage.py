import pytest

from todolist.storages.storage_implementation import StorageImplementation


@pytest.fixture
def categories():
    from todolist.tests.factory import CategoryFactory
    categories = CategoryFactory.create_batch(3)
    print(categories)
    from todolist.models import Category
    print(Category.objects.all())
    return categories


class TestAddNewTaskStorage:

    @pytest.mark.django_db
    def test_check_is_lable_valid(self):
        # Arrange
        lable_name = 'Amazon'
        storage = StorageImplementation()

        # Act
        response = storage.check_is_lable_valid(name=lable_name)

        assert response is False

    @pytest.mark.django_db
    def test_check_is_category_valid(self):
        # Arrange
        category_name = 'Shopping'
        storage = StorageImplementation()

        # Act
        response = storage.check_is_category_valid(name=category_name)

        # Assert
        assert response is False

    @pytest.mark.django_db
    def test_get_category(self, categories):
        # Arrange
        category_name = 'Category 1'
        storage = StorageImplementation()

        # Act
        # category_id = storage.get_category(name=category_name)

        # Assert
        # assert category_id == 1

    def test_get_lable(self):
        pass
