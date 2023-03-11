#!/usr/bin/python3
""" 5. LFU Caching
"""

from enum import Enum
from heapq import heappush, heappop
from itertools import count

BaseCaching = __import__("base_caching").BaseCaching


class HeapItemStatus(Enum):
    """ HeapItemStatus Enum
    """
    ACTIVE = 1
    INACTIVE = 2


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        """ Initialize the class
        """
        super().__init__()
        self.heap = []
        self.map = {}
        self.counter = count()

    def put(self, key, item):
        """ put method to add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.rehydrate(key)
            else:
                if self.is_full():
                    self.evict()
                self.add_to_heap(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get method to get an item by key """
        if key in self.cache_data:
            self.rehydrate(key)
            return self.cache_data.get(key)

    def is_full(self):
        """ check number of items  """
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        """ evict item from cache """
        while self.heap:
            _, __, item, status = heappop(self.heap)
            if status == HeapItemStatus.ACTIVE:
                print("DISCARD: " + str(item))
                del self.cache_data[item]
                return

    def rehydrate(self, key):
        """ Marks current item as inactive and reinserts updated count back
        into heap.
        """
        entry = self.map[key]
        entry[-1] = HeapItemStatus.INACTIVE
        self.add_to_heap(key, entry[0])

    def add_to_heap(self, key, count=0):
        """ Adds a new entry into a heap.
        """
        entry = [1 + count, next(self.counter), key, HeapItemStatus.ACTIVE]
        self.map[key] = entry
        heappush(self.heap, entry)
