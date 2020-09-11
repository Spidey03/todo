import abc


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def add_category(self, name: str):
        pass

    @abc.abstractmethod
    def add_lable(self, name: str):
        pass

    @abc.abstractmethod
    def check_is_lable_valid(self, name: str):
        pass

    @abc.abstractmethod
    def get_category(self, name: str):
        pass

    @abc.abstractmethod
    def check_is_category_valid(self, name: str):
        pass

    @abc.abstractmethod
    def get_lable(self, name):
        pass

    @abc.abstractmethod
    def add_new_task(self, title, content, category, lable, date):
        pass

    @abc.abstractmethod
    def get_tasks(self):
        pass

    @abc.abstractmethod
    def get_categories(self, category_ids):
        pass

    @abc.abstractmethod
    def get_lables_for_tasks(self, task_ids):
        pass
