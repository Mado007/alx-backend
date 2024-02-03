#!/usr/bin/env python3
""" MRUCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Defines a MRUCache caching system"""
    def __init__(self):
        """Init method."""
        super().__init__()
        self.recentNo = 0

    def put(self, key, item):
        """Assign `key` and `item` to the dictionary of cache_data."""
        if key and item:
            if key not in self.cache_data.keys() and\
               len(self.cache_data) == super().MAX_ITEMS:
                # sort cache items by recentNo
                sorted_items = sorted(self.cache_data.items(),
                                      key=lambda i: i[1][1])
                # discard the most recently used item
                discarded_key = sorted_items[-1][0]
                self.cache_data.pop(discarded_key)
                print(f'DISCARD: {discarded_key}')
            self.recentNo += 1
            self.cache_data[key] = [item, self.recentNo]

    def get(self, key):
        """Return the value linked to key from cache_data."""
        if not key or key not in self.cache_data:
            return None
        self.recentNo += 1
        self.cache_data.get(key)[1] = self.recentNo
        return self.cache_data.get(key)[0]
        # if `key` is not found,
        # dict.get() returns None by default
        # and doesn't raise KeyError

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)[0]))
