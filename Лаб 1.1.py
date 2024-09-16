"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self, list: list):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        :param list: Очередь, где list[0] - ее начало, list[-1] - ее конец
        """
        ...  # TODO инициализировать список
        self.list = list
    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        ...  # TODO реализовать метод enqueue
        return list.append(elem)  # сложность О(1)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        ...  # TODO реализовать метод dequeue
        if list == []:
            raise IndexError("Очередь пуста")
        return list.popleft() # cложность O(1)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        ...  # TODO реализовать метод peek
        return list[ind] # сложность О(n)

    def clear(self) -> None:
        """ Очистка очереди. """
        ...  # TODO реализовать метод clear
        return list.pop() # сложность О(n)

    def __len__(self):
        """ Количество элементов в очереди. """
        ...  # TODO реализовать метод __len__
        return len(list) # сложность О(n)



