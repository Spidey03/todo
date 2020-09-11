from todolist.constants.constants import StatusCode
from todolist.interactors.presenters.presenter_interface \
    import PresenterInterface


class PresenterImplementation(PresenterInterface):

    def successfully_created_category(self):
        from todolist.constants.exception_messages \
            import INVALID_CATEGORY_NAME_EXCEPTION
        response = INVALID_CATEGORY_NAME_EXCEPTION[0]
        res_status = INVALID_CATEGORY_NAME_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_invalid_category_name_exception(self):
        from todolist.constants.exception_messages \
            import CATEGORY_ADDED_SUCCESSFULLY
        response = CATEGORY_ADDED_SUCCESSFULLY[0]
        res_status = CATEGORY_ADDED_SUCCESSFULLY[1]
        http_status_code = StatusCode.Created_Success.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def successfully_created_lable(self):
        from todolist.constants.exception_messages \
            import LABLE_CREATED_SUCCESSFULLY
        response = LABLE_CREATED_SUCCESSFULLY
        res_status = LABLE_CREATED_SUCCESSFULLY[1]
        http_status_code = StatusCode.Created_Success.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_invalid_lable_name_exception(self):
        from todolist.constants.exception_messages \
            import INVALID_LABLE_NAME_EXCEPTION
        response = INVALID_LABLE_NAME_EXCEPTION[0]
        res_status = INVALID_LABLE_NAME_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_invalid_category_exception(self):
        from todolist.constants.exception_messages \
            import INVALID_CATEGORY_EXCEPTION
        response = INVALID_CATEGORY_EXCEPTION[0]
        res_status = INVALID_CATEGORY_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_invalid_lable_exception(self):
        from todolist.constants.exception_messages \
            import INVALID_LABLE_EXCEPTION
        response = INVALID_LABLE_EXCEPTION[0]
        res_status = INVALID_LABLE_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_invalid_value_for_title(self):
        from todolist.constants.exception_messages \
            import INVALID_VALUE_FOR_TITLE_EXCEPTION
        response = INVALID_VALUE_FOR_TITLE_EXCEPTION[0]
        res_status = INVALID_VALUE_FOR_TITLE_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_invalid_value_for_content(self):
        from todolist.constants.exception_messages \
            import INVALID_VALUE_FOR_CONTENT_EXCEPTION
        response = INVALID_VALUE_FOR_CONTENT_EXCEPTION[0]
        res_status = INVALID_VALUE_FOR_CONTENT_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def successfully_created_task(self):
        from todolist.constants.exception_messages \
            import TASK_ADDED_SUCCESSFULLY
        response = TASK_ADDED_SUCCESSFULLY[0]
        res_status = TASK_ADDED_SUCCESSFULLY[1]
        http_status_code = StatusCode.Created_Success.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def response_get_todos(self, task_details_dtos):
        tasks = []
        for task in task_details_dtos:
            tasks.append({
                'task_id': task.id,
                'title': task.title,
                'content': task.content,
                'category': task.category,
                'date': task.date,
                'lables': self._get_lables_for_task(
                    task.task_lables, task.id)
            })
        return tasks

    @staticmethod
    def _get_lables_for_task(task_lables, task_id):
        lables = [task_lable.lable_name for task_lable in task_lables
                  if task_id == task_lable.task_id]
        return lables
