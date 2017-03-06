class Node(object):

    def __init__(self, key, value):

        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):

        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.cache = {}
        self.cap = capacity
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, newnode):

        newnode.next = self.head.next
        newnode.prev = self.head
        self.head.next.prev = newnode
        self.head.next = newnode

    def remove(self, node):

        pre = node.prev
        nxt = node.next
        node.prev = None
        node.next = None
        pre.next = nxt
        nxt.prev = pre

    def get(self, key):

        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def set(self, key, value):

        if key not in self.cache:
            newnode = Node(key, value)
            self.add(newnode)
            self.cache[key] = newnode
            if len(self.cache) > self.cap:
                dumpnode = self.tail.prev
                self.remove(dumpnode)
                del self.cache[dumpnode.key]
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)



Sol = LRUCache(2)
Sol.set(2, 1241)
Sol.set(3, 13)
Sol.set(4, 124)
print Sol.get(3)
Sol.set(5, 314)


'''
# the insert/pop item from OrderedDict is theoretically O(1), because it's
# implemented by two hashtables and a doubly-linked list at the bottom level
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):

        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):

        if key not in self.cache:
            return -1
        else:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value

    def set(self, key, value):

        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last = False)
'''

