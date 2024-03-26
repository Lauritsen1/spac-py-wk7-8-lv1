from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Repository(ABC, Generic[T]):

    @abstractmethod
    def get(self, id: str) -> T:
        pass

    @abstractmethod
    def get_all(self) -> list[T]:
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
