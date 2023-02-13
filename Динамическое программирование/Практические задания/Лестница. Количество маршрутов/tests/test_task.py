import unittest

from task import stairway_path


class TestCase(unittest.TestCase):
    def test_zero_stair(self):
        self.assertEqual(
            1, stairway_path(0),
            msg=f"Нет ступеней - один маршрут до вершины :)"
        )

    def test_count_paths(self):
        count_paths = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
        for count_stairs, count_paths in enumerate(count_paths):
            with self.subTest(count_stairs=count_stairs):
                self.assertEqual(
                    count_paths, stairway_path(count_stairs),
                    msg=f"Не правильно :( До ступени {count_stairs} количество маршрутов должно быть {count_paths}."
                )

    def test_negative_stair(self):
        with self.assertRaises(ValueError, msg="Что такое отрицательное количество ступеней? Должна вызываться ошибка"):
            stairway_path(-35)
