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
    def response_get_todos(self, task_details_dtos):
        pass

    @abc.abstractmethod
    def raise_invalid_value_for_title(self):
        pass

    @abc.abstractmethod
    def raise_invalid_value_for_content(self):
        pass