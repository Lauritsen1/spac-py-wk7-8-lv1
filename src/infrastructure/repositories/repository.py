from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def get(self, entity):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass
