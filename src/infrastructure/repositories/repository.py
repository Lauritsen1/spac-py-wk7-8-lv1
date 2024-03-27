from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Repository(ABC, Generic[T]):

    @abstractmethod
    def find(self, id: str) -> T:
        pass

    @abstractmethod
    def find_many(self) -> list[T]:
        pass

    @abstractmethod
    def add(self, entity: T) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def delete(self, id: str) -> T:
        pass
