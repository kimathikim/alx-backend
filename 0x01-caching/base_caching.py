#!/usr/bin/env python3
"""BaseCaching module"""


class BaseCaching:
    """BaseCaching defines:
    - constants of your caching system
    - where methods are shared between
      the caching system
    """

    MAX_ITEMS = 4

    def __init__(self):
        """Initiliaze"""
        self.cache_data = {}

    def print_cache(self):
        """Print the cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache"""
        raise NotImplementedError("Put method must be implemented in your cache class")

    def get(self, key):
        """Get An item by Key"""
        raise NotImplementedError("Get method must be implemented in your cache class")

