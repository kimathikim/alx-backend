#!/usr/bin/env python3
"""This module implements the LIFO caching algorithm"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This class implements the LIFO caching system"""

    def __init__(self) -> None:
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item) -> None:
        """This method add data into the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # update the item
            self.cache_data[key] = item
            self.queue.remove(key)
            self.queue.append(key)

            # THE algorithm
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.queue.pop(-1)
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """This function defined the method that gets data from the cache"""
        # check if the cache exists or if it is null
        if key in self.cache_data or key is None:
            return None

        return self.cache_data.get(key)
