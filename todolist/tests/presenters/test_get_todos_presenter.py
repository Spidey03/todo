import datetime

import pytest
from freezegun import freeze_time

from todolist.presenters.presenter_implementation \
    import PresenterImplementation

@freeze_time("2012-01-14")
class TestGetTodosPresenter:
    @pytest.fixture()
    def todos_response(self):
        expected_output = [
            {
                'task_id': 0,
                'title': 'Title 000',
                'content': 'Content 000',
                'category': 'Category 0',
                'date': '2020-01-01',
                'lables': []
            },
            {
                'task_id': 1,
                'title': 'Title 001',
                'content': 'Content 001',
                'category': 'Category 1',
                'date': '2020-01-01',
                'lables': []
            }
        ]
        return expected_output

    @pytest.fixture()
    def task_details_dto(self):
        from todolist.tests.common_fixtures.factories import TaskDetailsDTOFactory
        task_details_dto = TaskDetailsDTOFactory.create_batch(2, date=datetime.date(2020, 1, 1))
        return task_details_dto

    def test_response_get_todos(self, task_details_dto, todos_response):
        # Arrange
        presenter = PresenterImplementation()
        expected_output = todos_response

        # Act
        response = presenter.response_get_tasks(task_details_dto)

        # Assert
        assert response == expected_output