from typing import Tuple
from functools import lru_cache


def calculate_paths(shape: Tuple[int, int]) -> int:
    """
    Дано поле с размером rows*cols посчитать количество ходов коня из верхнего левого угла в нижний правый

    :param shape: размер доски в виде кортежа
    :return: количество путей согласно заданным условиям
    """
    rows, cols = shape  # кол-во строк и столбцов отсчет с 1

    @lru_cache  # @lru_cache(maxsize=None) == lru_cache
    def get_steps(i, j):
        if i == 0 and j == 0:  # левый верхний угол
            return 1

        if not 0 <= i < rows:  # выпадаю за границы поля для строк
            return 0

        if not 0 <= j < cols:  # выпадаю за границы поля для строк
            return 0

        return sum([
            get_steps(i - 2, j + 1),
            get_steps(i - 2, j - 1),
            get_steps(i - 1, j - 2),
            get_steps(i + 1, j - 2),
        ])

    return get_steps(rows-1, cols-1)


if __name__ == '__main__':
    print(calculate_paths((4, 4)))  # 2
    print(calculate_paths((7, 15)))  # 13309
