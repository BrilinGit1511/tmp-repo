from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами
    minimum = min(container)
    maximum = max(container)
    dict_value = {key: 0 for key in range(minimum, maximum+1)}
    sorted_array = []
    for value in container:
            dict_value[value]+=1
    for key, value in dict_value.items():
        for i in range(value):
            sorted_array.append(key)

    return sorted_array


if __name__ == "__main__":
    print(sort([1, 4, 3, 2, 2, 4, 1]))




