import abc


class PresenterInterface(abc.ABC):

    @abc.abstractmethod
    def successfully_created_category(self):
        pass

    @abc.abstractmethod
    def raise_invalid_category_name_exception(self):
        pass

    @abc.abstractmethod
    def successfully_created_lable(self):
        pass

    @abc.abstractmethod
    def raise_invalid_lable_name_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_category_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_lable_exception(self):
        pass

    @abc.abstractmethod
    def successfully_created_task(self):
        pass

    @abc.abstractmethod
    def response_get_tasks(self, task_details_dtos):
        pass

    @abc.abstractmethod
    def raise_invalid_value_for_title(self):
        pass

    @abc.abstractmethod
    def raise_invalid_value_for_content(self):
        pass

    @abc.abstractmethod
    def response_get_categories(self, category_dtos):
        pass

    @abc.abstractmethod
    def resposne_get_task(self, task_details_dto):
        pass

    @abc.abstractmethod
    def raise_user_does_not_exist(self):
        pass

    @abc.abstractmethod
    def raise_password_is_incorrect(self):
        pass

    @abc.abstractmethod
    def get_response_login_user(self, tokens_dto):
        pass

    @abc.abstractmethod
    def user_created_successfully(self):
        pass

    @abc.abstractmethod
    def raise_username_should_not_be_empty(self):
        pass

    @abc.abstractmethod
    def raise_email_is_invalid(self):
        pass

    @abc.abstractmethod
    def raise_bio_is_empty(self):
        pass

    @abc.abstractmethod
    def raise_password_not_match_to_constraints(self):
        pass

    @abc.abstractmethod
    def raise_passwords_should_be_identical(self):
        pass

    @abc.abstractmethod
    def raise_username_already_taken(self):
        pass

    @abc.abstractmethod
    def raise_user_already_register_with_this_email(self):
        pass

    @abc.abstractmethod
    def response_get_profile(self, user_details_dto):
        pass

    @abc.abstractmethod
    def raise_task_not_found_exception(self):
        pass