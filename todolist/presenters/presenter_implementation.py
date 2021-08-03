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

    def successfully_updated_task(self):
        from todolist.constants.exception_messages \
            import TASK_UPDATED_SUCCESSFULLY
        response = TASK_UPDATED_SUCCESSFULLY[0]
        res_status = TASK_UPDATED_SUCCESSFULLY[1]
        http_status_code = StatusCode.Success.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def response_get_tasks(self, task_details_dtos):
        tasks = []
        for task in task_details_dtos:
            tasks.append(self._get_task_details(task_details_dto=task))
        return {
            'response': {
                "tasks": tasks
            },
            'status_code': 200
        }

    @staticmethod
    def _get_lables_for_task(task_lables, task_id):
        lables = [task_lable.lable_name for task_lable in task_lables
                  if task_id == task_lable.task_id]
        return lables

    def response_get_categories(self, category_dtos):
        categories = []
        for category_dto in category_dtos:
            categories.append({
                'category_id': category_dto.id,
                'name': category_dto.name
            })
        return categories

    def resposne_get_task(self, task_details_dto):
        task_details = self._get_task_details(
            task_details_dto=task_details_dto)
        return task_details

    def _get_task_details(self, task_details_dto):
        task_details = {
            'task_id': task_details_dto.id,
            'title': task_details_dto.title,
            'content': task_details_dto.content,
            'category': task_details_dto.category,
            'date': str(task_details_dto.date),
            'lables': self._get_lables_for_task(
                task_details_dto.task_lables, task_details_dto.id)
        }
        return task_details

    def raise_user_does_not_exist(self):
        from todolist.constants.exception_messages \
            import INVALID_USERNAME
        response = INVALID_USERNAME[0]
        res_status = INVALID_USERNAME[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_password_is_incorrect(self):
        from todolist.constants.exception_messages \
            import INVALID_PASSWORD
        response = INVALID_PASSWORD[0]
        res_status = INVALID_PASSWORD[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def get_response_login_user(self, tokens_dto):
        response = {
            "user_id": tokens_dto.user_id,
            "access_token": tokens_dto.access_token,
            "refresh_token": tokens_dto.refresh_token,
            "expires_in": tokens_dto.expires_in,
            "status_code": StatusCode.Success.value
        }
        return response

    def user_created_successfully(self):
        from todolist.constants.exception_messages \
            import USER_CREATED_SUCCESSFULLY
        response = USER_CREATED_SUCCESSFULLY[0]
        res_status = USER_CREATED_SUCCESSFULLY[1]
        http_status_code = StatusCode.Created_Success.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_username_should_not_be_empty(self):
        from todolist.constants.exception_messages \
            import USERNAME_SHOULD_NOT_BE_EMPTY
        response = USERNAME_SHOULD_NOT_BE_EMPTY[0]
        res_status = USERNAME_SHOULD_NOT_BE_EMPTY[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_email_is_invalid(self):
        from todolist.constants.exception_messages \
            import EMAIL_SHOULD_BE_VALID
        response = EMAIL_SHOULD_BE_VALID[0]
        res_status = EMAIL_SHOULD_BE_VALID[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_bio_is_empty(self):
        from todolist.constants.exception_messages \
            import BIO_SHOULD_NOT_BE_EMPTY
        response = BIO_SHOULD_NOT_BE_EMPTY[0]
        res_status = BIO_SHOULD_NOT_BE_EMPTY[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_password_not_match_to_constraints(self):
        from todolist.constants.exception_messages \
            import PASSWORD_SHOLUD_MATCH_CONSTRAINTS
        response = PASSWORD_SHOLUD_MATCH_CONSTRAINTS[0]
        res_status = PASSWORD_SHOLUD_MATCH_CONSTRAINTS[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_passwords_should_be_identical(self):
        from todolist.constants.exception_messages \
            import PASSWORD_SHOULD_BE_IDENTICAL
        response = PASSWORD_SHOULD_BE_IDENTICAL[0]
        res_status = PASSWORD_SHOULD_BE_IDENTICAL[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_username_already_taken(self):
        from todolist.constants.exception_messages \
            import USERNAME_ALREADY_TAKEN
        response = USERNAME_ALREADY_TAKEN[0]
        res_status = USERNAME_ALREADY_TAKEN[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def raise_user_already_register_with_this_email(self):
        from todolist.constants.exception_messages \
            import USER_ALREADY_REGISTERED_WITH_THIS_EMAIL
        response = USER_ALREADY_REGISTERED_WITH_THIS_EMAIL[0]
        res_status = USER_ALREADY_REGISTERED_WITH_THIS_EMAIL[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

    def response_get_profile(self, user_details_dto):
        user = {
            "id": user_details_dto.user_id,
            "name": user_details_dto.username,
            "email": user_details_dto.email,
            "bio": user_details_dto.bio,
            "firstname": user_details_dto.firstname,
            "lastname": user_details_dto.lastname,
            "profile_pic": user_details_dto.profile_pic
        }
        return user

    def raise_task_not_found_exception(self):
        from todolist.constants.exception_messages \
            import TASK_NOT_FOUND
        response = TASK_NOT_FOUND[0]
        res_status = TASK_NOT_FOUND[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }