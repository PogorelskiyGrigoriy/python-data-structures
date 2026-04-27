import unittest
from my_lru_cache import MyLruCache

class TestMyLruCache(unittest.TestCase):
    def setUp(self):
        """Initialize a fresh cache instance before each test"""
        self.capacity = 3
        self.cache = MyLruCache[str, int](self.capacity)

    def test_invalid_init(self):
        """Ensure invalid capacity raises ValueError"""
        with self.assertRaises(ValueError):
            MyLruCache(0)

    def test_basic_ops(self):
        """Verify standard dictionary-like access"""
        self.cache["a"] = 100
        self.assertEqual(self.cache["a"], 100)
        self.assertTrue("a" in self.cache)
        self.assertEqual(len(self.cache), 1)

    def test_get_method(self):
        """Verify the safe .get() method behavior"""
        self.cache["a"] = 1
        self.assertEqual(self.cache.get("a"), 1)
        self.assertIsNone(self.cache.get("missing"))
        self.assertEqual(self.cache.get("missing", 404), 404)

    def test_eviction(self):
        """Check if the oldest item is removed when capacity is exceeded"""
        self.cache["a"] = 1
        self.cache["b"] = 2
        self.cache["c"] = 3
        self.cache["d"] = 4  # This should evict 'a'
        
        self.assertNotIn("a", self.cache)
        self.assertIn("d", self.cache)
        self.assertEqual(len(self.cache), 3)

    def test_priority_update(self):
        """Verify that accessing an item prevents its eviction"""
        self.cache["a"] = 1
        self.cache["b"] = 2
        self.cache["c"] = 3
        
        # Accessing 'a' makes it the most recent
        _ = self.cache["a"]
        
        # Adding 'd' should now evict 'b' instead of 'a'
        self.cache["d"] = 4
        
        self.assertIn("a", self.cache)
        self.assertNotIn("b", self.cache)

    def test_iteration_order(self):
        """Verify keys are yielded from oldest to newest"""
        self.cache["a"] = 1
        self.cache["b"] = 2
        self.cache["c"] = 3
        self.cache["a"] = 10  # Update 'a' to make it most recent
        
        self.assertEqual(list(self.cache), ["b", "c", "a"])

    def test_clear(self):
        """Ensure clear() empties the collection"""
        self.cache["a"] = 1
        self.cache.clear()
        self.assertEqual(len(self.cache), 0)

if __name__ == "__main__":
    unittest.main()