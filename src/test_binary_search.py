import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_found_middle(self):
        """Элемент находится в середине списка"""
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_found_start(self):
        """Элемент находится в самом начале"""
        self.assertEqual(binary_search([10, 20, 30], 10), 0)

    def test_found_end(self):
        """Элемент находится в самом конце"""
        self.assertEqual(binary_search([10, 20, 30], 30), 2)

    def test_not_found_smaller(self):
        """Элемент меньше всех в списке (должен вернуть -(0 + 1) = -1)"""
        self.assertEqual(binary_search([10, 20, 30], 5), -1)

    def test_not_found_larger(self):
        """Элемент больше всех в списке (должен вернуть -(3 + 1) = -4)"""
        self.assertEqual(binary_search([10, 20, 30], 40), -4)

    def test_not_found_between(self):
        """Элемент отсутствует, но находится внутри диапазона (-(1 + 1) = -2)"""
        self.assertEqual(binary_search([10, 20, 30], 15), -2)

    def test_empty_list(self):
        """Поиск в пустом списке (-(0 + 1) = -1)"""
        self.assertEqual(binary_search([], 10), -1)

    def test_single_element_found(self):
        """Список из одного элемента (найден)"""
        self.assertEqual(binary_search([42], 42), 0)

    def test_single_element_not_found(self):
        """Список из одного элемента (не найден)"""
        # Если ищем 50 в [42], low станет 1. Результат -(1 + 1) = -2
        self.assertEqual(binary_search([42], 50), -2)
        # Если ищем 10 в [42], low останется 0. Результат -(0 + 1) = -1
        self.assertEqual(binary_search([42], 10), -1)

    def test_duplicates(self):
        """Работа с дубликатами (должен вернуть любой валидный индекс)"""
        res = binary_search([1, 2, 2, 2, 3], 2)
        self.assertIn(res, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()