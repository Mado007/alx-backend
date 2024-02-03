#!/usr/bin/env python3
""" BasicCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Defines the caching system"""
    def put(self, key, item):
        """Assign `key` and `item` to the dictionary of cache_data."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key from cache_data."""
        if not key:
            return None

        return self.cache_data.get(key)
        # if `key` is not found,
        # dict.get() returns None by default
        # and doesn't raise KeyError
