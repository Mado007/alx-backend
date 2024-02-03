#!/usr/bin/env python3
""" LFUCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Defines a LFUCache caching system"""
    def put(self, key, item):
        """Assign `key` and `item` to the dictionary of cache_data."""
        if key and item:
            if key not in self.cache_data.keys() and\
               len(self.cache_data) == super().MAX_ITEMS:
                # sort cache items by frequencyNo
                sorted_items = sorted(self.cache_data.items(),
                                      key=lambda i: i[1][1])
                # discard the most recently used item
                discarded_key = sorted_items[0][0]
                self.cache_data.pop(discarded_key)
                print(f'DISCARD: {discarded_key}')

            if key in self.cache_data:
                freq = self.cache_data[key][1]
                self.cache_data[key] = [item, freq + 1]
            else:
                self.cache_data[key] = [item, 1]

    def get(self, key):
        """Return the value linked to key from cache_data."""
        if not key or key not in self.cache_data:
            return None

        self.cache_data.get(key)[1] += 1
        return self.cache_data.get(key)[0]

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)[0]))
