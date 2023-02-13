from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    left_border = 0
    right_border = len(seq) - 1

    while left_border <= right_border:
        middle_index = left_border + (right_border - left_border) // 2
        middle_value = seq[middle_index]
        if value == middle_value:
            while True:
                if not 0 <= middle_index - 1 < len(seq) or seq[middle_index - 1] != value:
                    break
                else:
                    middle_index -= 1
            return middle_index
        elif middle_value > value:
            right_border = middle_index - 1
        else:
            left_border = middle_index + 1

    raise ValueError(f"Элемента {value} нет")
