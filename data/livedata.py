from typing import TypeVar, Generic

T = TypeVar('T')


class LiveData(Generic[T]):
    def __init__(self, value: T):
        self._value = value
        self.__observers = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: T):
        self._value = value
        for observer in self.__observers:
            observer(self._value)

    def observe(self, observer):
        self.__observers.append(observer)

    def clear_observers(self):
        self.__observers.clear()

    def __repr__(self):
        return f'LiveData({self._value})'
