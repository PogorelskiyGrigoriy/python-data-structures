import unittest
from binary_search import insort

class TestInsort(unittest.TestCase):

    def test_insert_into_empty_list(self):
        """Вставка в пустой список"""
        self.assertEqual(insort([], 5), [5])

    def test_insert_at_start(self):
        """Вставка элемента, который меньше всех существующих"""
        self.assertEqual(insort([10, 20, 30], 5), [5, 10, 20, 30])

    def test_insert_at_end(self):
        """Вставка элемента, который больше всех существующих"""
        self.assertEqual(insort([10, 20, 30], 40), [10, 20, 30, 40])

    def test_insert_in_middle(self):
        """Вставка элемента в середину списка"""
        self.assertEqual(insort([10, 20, 30], 15), [10, 15, 20, 30])

    def test_insert_duplicate(self):
        """Вставка элемента, который уже есть в списке"""
        self.assertEqual(insort([1, 2, 3], 2), [1, 2, 2, 3])

    def test_insert_all_same_elements(self):
        """Вставка в список, состоящий из одинаковых элементов"""
        self.assertEqual(insort([2, 2, 2], 2), [2, 2, 2, 2])

    def test_in_place_modification(self):
        """Проверка того, что функция модифицирует исходный список"""
        original_list = [10, 30]
        insort(original_list, 20)
        self.assertEqual(original_list, [10, 20, 30])

    def test_large_integers(self):
        """Вставка больших чисел"""
        self.assertEqual(insort([10**10, 10**12], 10**11), [10**10, 10**11, 10**12])

    def test_negative_numbers(self):
        """Работа с отрицательными числами"""
        self.assertEqual(insort([-30, -10], -20), [-30, -20, -10])

if __name__ == '__main__':
    unittest.main()