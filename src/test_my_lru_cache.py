from unittest import TestCase
from my_lru_cache import MyLruCache

numbers = [1, 20, 10]
class TestLruCache(TestCase):
    cache:MyLruCache[int, int]
    
    def setUp(self):
        self.cache = MyLruCache(3)
        for num in numbers:
            self.cache.add(num, num ** 2)
            
    def test_add_exceeding_maxsize(self):
        self.cache.add(5, 25)
        self.assertEqual(25, self.cache.access(5))
        with self.assertRaises(KeyError):
            self.cache.access(1)
            
    def test_access_ordering(self):
        self.assertEqual(1, self.cache.access(1))
        self.assertEqual(400, self.cache.access(20))
        self.cache.add(5, 25)
        self.assertEqual(25, self.cache.access(5))
        self.assertEqual(1, self.cache.access(1))
        self.assertEqual(400, self.cache.access(20))
        with self.assertRaises(KeyError):
            self.cache.access(10)           