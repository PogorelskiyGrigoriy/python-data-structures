from collections import OrderedDict
from collections.abc import Hashable
from typing import Generic, TypeVar, Optional, Iterator

# K is restricted to Hashable types to be used as a dictionary key
K = TypeVar("K", bound=Hashable)
V = TypeVar("V")

class MyLruCache(Generic[K, V]):
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.cache: OrderedDict[K, V] = OrderedDict()

    def __getitem__(self, key: K) -> V:
        """Access item using bracket notation: value = cache[key]"""
        if key not in self.cache:
            raise KeyError(f"Key {key} not found")
        # Move accessed item to the end to mark it as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def __setitem__(self, key: K, value: V) -> None:
        """Add or update item: cache[key] = value"""
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # Evict the oldest item if capacity is exceeded
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        """Safely retrieve an item without raising KeyError"""
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key: object) -> bool:
        """Check existence: 'key' in cache (O(1) complexity)"""
        return key in self.cache

    def __iter__(self) -> Iterator[K]:
        """Iterate through keys from oldest to newest"""
        return iter(self.cache)

    def __len__(self) -> int:
        """Return current number of items in cache"""
        return len(self.cache)

    def clear(self) -> None:
        """Remove all items from the cache"""
        self.cache.clear()

    def __repr__(self) -> str:
        """Developer-friendly string representation"""
        return f"MyLruCache(capacity={self.capacity}, size={len(self.cache)})"