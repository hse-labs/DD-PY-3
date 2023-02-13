from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return container

    def _merge(left_container: List[int], right_container: List[int]) -> List[int]:
        """
        1. Берем два отсортированных массива
        2. Сравниваем первые элементы из каждого массива и в итоговый массив записываем наименьшее
        3. В массиве, в котором был наименьший элемент, переходим к следующему
        4. Когда один из массивов закончится, остаток второго «сливаем» в итоговый массив

        :param left_container: Левый отсортированный массива
        :param right_container: Правый отсортированный массива

        :return: Результат слияния двух отсортированных массивов, как новый отсортированный массив
        """
        merged_container = []

        while True:
            # 2. сравниваем первые элементы из каждого массива и в итоговый массив записываем наименьшее
            if left_container[0] <= right_container[0]:
                elem = left_container.pop(0)  # 3. в массиве, в котором был наименьший элемент, переходим к следующему
                merged_container.append(elem)
            else:
                elem = right_container.pop(0)  # 3. в массиве, в котором был наименьший элемент, переходим к следующему
                merged_container.append(elem)

            # 4. когда один из массивов закончится, остаток второго «сливаем» в итоговый массив
            if not left_container:
                merged_container += right_container
                break
            if not right_container:
                merged_container += left_container
                break

        return merged_container

    if len(container) == 1:  # 1. Если массив состоит из 1 элемента – он отсортирован
        return container

    middle = len(container) // 2  # 2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    new_left = sort(container[:middle])
    new_right = sort(container[middle:])

    # 3. После сортировки двух частей массива к ним применяется процедура слияния
    return _merge(new_left, new_right)
