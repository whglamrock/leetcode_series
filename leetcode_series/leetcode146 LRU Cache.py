
# doubly-linked listnode

class Node:
    def __init__(self, key, val):

        self.key = key
        self.val = val
        self.prev = None
        self.next = None


# idea: implement the OrderedDict data structure ourselves
# the key is to put the self.cache[key] = node into the add function and del self.cache[key] into remove function

class LRUCache(object):

    def __init__(self, capacity):

        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.cap = capacity
        self.keytonode = {}
        self.size = 0

    def add(self, node):

        oldfirstnode = self.head.next
        node.prev, node.next = self.head, oldfirstnode
        self.head.next, oldfirstnode.prev = node, node
        key = node.key
        self.keytonode[key] = node

    # name the function as "remove" instead of "pop", because it's not simply popping the last item
    def remove(self, node):

        key = node.key
        del self.keytonode[key]
        prevnode, nextnode = node.prev, node.next
        node.prev, node.next = None, None
        prevnode.next, nextnode.prev = nextnode, prevnode

    def get(self, key):

        if key not in self.keytonode:
            return -1
        else:
            node = self.keytonode[key]
            self.remove(node)
            self.add(node)
            return node.val

    def put(self, key, value):

        if key in self.keytonode:   # the size won't change
            node = self.keytonode[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if self.size == self.cap:
                # no need to consider the case when self.tail.prev == self.head
                lastnode = self.tail.prev
                self.remove(lastnode)
                self.size -= 1
            newnode = Node(key, value)
            self.add(newnode)
            self.size += 1



Sol = LRUCache(2)
Sol.put(2, 1241)
Sol.put(3, 13)
Sol.put(4, 124)
print Sol.get(3)
Sol.put(5, 314)



'''
from collections import OrderedDict

# the insert/pop item from OrderedDict is O(1)
# P.S. remember all O(1) hashtable operations are theoretical

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

    def put(self, key, value):

        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last = False)
'''

