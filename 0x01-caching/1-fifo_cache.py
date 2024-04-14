#!/usr/bin/env python3

"""This module contains the implementation fo the FIFO Class"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This class implements the FIFO caching system"""

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """This function defines how th add data into the system"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.queue.pop(0)
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """This function defines how to get data from the system"""
        if key is None or key not in self.cache_data:
            return None
        print(self.cache_data)
