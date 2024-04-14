#!/usr/bin/env python3
"""This moodule contains the LFU Cache implementation"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """This class implements the LFU caching system"""

    def __init__(self):
        """Initializes the LFU caching system"""
        super().__init__()
        self.lfu = []

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lfu.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discard = self.lfu.pop(0)
                    del self.cache_data[discard]
                    print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.lfu.append(key)
        self.lfu.sort(key=lambda k: self.cache_data[k])

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is not None and key in self.cache_data:
            self.lfu.remove(key)
            self.lfu.append(key)
            return self.cache_data[key]
        return None
        return None
