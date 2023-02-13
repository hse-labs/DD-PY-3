from typing import List


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    table = table.copy()
    n = len(table)
    m = len(table[0])

    # Цикл по первому столбцу
    for row_index in range(n - 1):
        table[row_index + 1][0] += table[row_index][0]
    # Цикл по первой строке
    for col_index in range(m - 1):
        table[0][col_index + 1] += table[0][col_index]

    for i in range(1, n):
        for j in range(1, m):
            table[i][j] += min(table[i - 1][j], table[i][j - 1])

    return table


if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    print(total_coasts[-1][-1])  # 21
