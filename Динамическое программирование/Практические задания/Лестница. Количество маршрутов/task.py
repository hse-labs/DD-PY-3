def stairway_path(count_stairs: int) -> int:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до вершины
    """
    if count_stairs < 0:
        raise ValueError("Количество ступеней должно быть не отрицательным числом")

    if count_stairs == 0:
        return 1

    if count_stairs == 1:
        return 2

    count_paths = [0] * (count_stairs + 1)
    count_paths[0] = 1
    count_paths[1] = 2

    for i in range(2, count_stairs + 1):  # начиная с 2 до n включительно
        count_paths[i] = count_paths[i-1] + count_paths[i-2]

    return count_paths[-1]


if __name__ == '__main__':
    print(stairway_path(0))  # 1
    print(stairway_path(5))  # 13
