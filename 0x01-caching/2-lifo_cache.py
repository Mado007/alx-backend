#!/usr/bin/env python3
""" LIFOCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Defines a LIFO caching system"""
    def put(self, key, item):
        """Assign `key` and `item` to the dictionary of cache_data."""
        if key and item:
            if key not in self.cache_data.keys() and\
               len(self.cache_data) == super().MAX_ITEMS:
                # Discard the last added item
                discarded_item = self.cache_data.popitem()
                print(f'DISCARD: {discarded_item[0]}')
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key from cache_data."""
        if not key:
            return None

        return self.cache_data.get(key)
        # if `key` is not found,
        # dict.get() returns None by default
        # and doesn't raise KeyError
