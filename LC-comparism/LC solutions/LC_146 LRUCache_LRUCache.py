# LC_146 LRUCache_LRUCache
import collections
from typing import OrderedDict

from anyio import create_capacity_limiter

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last = False)
        self.cache[key] = value

#---------------------another approach-------------------------#

class Node:

    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = self.next = None

class LSUCache:
    def __init__(self, capacity:int) -> None:
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)                # left = LSU, right = most recent
        self.left.next, self.right.prev = self.right, self.left     # next and prev pointer point to each other

    def remove(self, node):
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev =nxt, prev

    def get(self, key:int)->int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self,key:int, value:int)->None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)           # map the node to this key
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:

            lru = self.left.next                    # an object of Node(key, val) indicate 
            self.remove(lru)
            del self.cache[lru.key]                 # remove the key of lru from hashmap


#-------------------one of online solution------------------#
class LRUCache:
    class _Node:
        __slots__ = 'key', 'val', 'prev', 'next'
        
        def __init__(self, key = None, val = None, prev = None, next = None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.mappings = {}
        self.header = self._Node()
        self.tailer = self._Node()
        self.header.next = self.tailer
        self.tailer.prev = self.header
        
    def _add_node_to_head(self, node):
        old_head = self.header.next
        self.header.next = node
        node.prev = self.header
        old_head.prev = node
        node.next = old_head
        self.length += 1
        return node
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.length -= 1
        return node
    
    def _eject_tail(self):
        if self.length > 0:
            ejected_node = self.tailer.prev
            ejected_node.prev.next = self.tailer
            self.tailer.prev = ejected_node.prev
            ejected_node.next = None
            ejected_node.prev = None
            self.length -= 1
            return ejected_node

    def get(self, key: int) -> int:
        if key in self.mappings:
            node = self.mappings[key]
            self._remove_node(node)
            self._add_node_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mappings:
            node = self.mappings[key]
            node.val = value
            self._remove_node(node)
            self._add_node_to_head(node)
        else:
            node = self._Node(key, value)
            self.mappings[key] = node
            self._add_node_to_head(node)
            if self.length > self.capacity:
                ejected_node = self._eject_tail()
                del self.mappings[ejected_node.key]