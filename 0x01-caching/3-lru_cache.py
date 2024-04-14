#!/usr/bin/env python3
"""This moodule contains the LRU Cache implementation"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This class implements the LRU caching system"""

    def __init__(self):
        """Initiliazes the LRU Cache instance"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """This method adds items into the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)

        elif len(self.order) >= BaseCaching.MAX_ITEMS:
            removed = self.order.pop(0)
            del self.cache_data[removed]
            print("DISCARD: {}".format(removed))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """This method gets the values from a specific part of the cache"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
        return None
