
# implementing the OrderedSet needs doubly-linked list, the head stores the most recent key

class Node:
    def __init__(self, key, val):

        self.key = key
        self.val = val
        self.prev = None
        self.next = None


# manually implement the OrderedSet

class OrderedSet:
    def __init__(self):

        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.keytonode = {}

    def size(self):

        return len(self.keytonode)

    def check(self, key):

        return key in self.keytonode

    # add to the head
    def add(self, key, val):

        newnode = Node(key, val)
        oldfirstnode = self.head.next
        newnode.prev, newnode.next = self.head, oldfirstnode
        self.head.next, oldfirstnode.prev = newnode, newnode
        self.keytonode[key] = newnode

    def delete(self, key):

        # put the hash deletion first
        node = self.keytonode[key]
        del self.keytonode[key]

        # disconnect the node from the doubly-linked list
        prevnode, nextnode = node.prev, node.next
        node.prev, node.next = None, None
        prevnode.next, nextnode.prev = nextnode, prevnode

        # to return is to provide input for other adding function
        return key, node.val

    def pop(self):

        # trivial check for corner case
        lastnode = self.tail.prev
        if lastnode.key == None:    # means it's self.head
            return

        lastkey = lastnode.key
        if lastkey in self.keytonode:
            del self.keytonode[lastkey]

        # disconnect the lastnode
        thenodepriortolastnode = lastnode.prev
        lastnode.prev, lastnode.next = None, None
        thenodepriortolastnode.next, self.tail.prev = self.tail, thenodepriortolastnode


# if the interviewer didn't ask, we use the built-in OrderedDict first;
#   otherwise manually implement the OrderedSet data structure

class LRUCache(object):
    def __init__(self, capacity):

        self.cap = capacity
        self.cache = OrderedSet()

    def get(self, key):

        if not self.cache.check(key):
            return -1
        else:
            key, val = self.cache.delete(key)
            self.cache.add(key, val)
            return val

    def put(self, key, value):

        if self.cache.check(key):
            self.cache.delete(key)
            self.cache.add(key, value)
        else:
            # remember the "size()" is a function of OrderedSet class, not a feature
            if self.cache.size() == self.cap:
                self.cache.pop()
            self.cache.add(key, value)



Sol = LRUCache(2)
Sol.put(2, 1241)
Sol.put(3, 13)
Sol.put(4, 124)
print Sol.get(3)
print Sol.get(2)
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
            del self.cache[key]  # it contains the operation of removing last node
            self.cache[key] = value  # add a node to the head
            return value

    def put(self, key, value):

        if key in self.cache:
            del self.cache[key]  # it will remove the node from the doubly-linked list as well
        self.cache[key] = value
        if len(self.cache) > self.cap:  # the len operation takes O(1)
            self.cache.popitem(last = False)
'''

