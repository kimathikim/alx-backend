#!/usr/bin/env python3
"""This module implement the caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BaseCache class"""

    def __init__(self):
        """Initiliaze"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get item from the cache using the key"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)