from collections import OrderedDict

class Node(object):

    def __init__(self, count):

        self.count = count
        self.keys = OrderedDict()
        self.prev = None
        self.next = None


class LFUCache(object):

    def __init__(self, capacity):

        self.cap = capacity
        self.valuehash = {}
        self.nodehash = {}
        self.head = None

    # when it's a completely new key that never appeared before
    def addToHead(self, key):

        if self.head == None:
            self.head = Node(1)
            # "= 0" means nothing, just need to add the key into OrderedDict
            self.head.keys[key] = 0
        elif self.head.count > 1:
            newhead = Node(1)
            newhead.next = self.head
            self.head.prev = newhead
            self.head = newhead
            self.head.keys[key] = 0
        else:
            self.head.keys[key] = 0
        self.nodehash[key] = self.head

    # when the number of keys with this count == 0
    def remove(self, node):

        p, n = node.prev, node.next
        if node == self.head:   # p = None
            self.head.next = None
            if n: n.prev = None
            self.head = n
        else:
            p.next = n
            if n: n.prev = p
            node.prev, node.next = None, None

    # remove the key with the least frequent count.
    def removeOld(self):

        if self.head == None: return
        old = None
        if len(self.head.keys) > 0:
            # the popped item from a dict, old, is represented as a tuple
            old = self.head.keys.popitem(last = False)
        if len(self.head.keys) == 0:
            self.remove(self.head)

        if old == None: return
        # old[0] is the popped key
        if old[0] in self.nodehash:
            del self.nodehash[old[0]]
        if old[0] in self.valuehash:
            del self.valuehash[old[0]]

    def increaseCount(self, key):

        node = self.nodehash[key]
        del node.keys[key]

        # we need "thenodewith(count+1).keys[key] = 0", then comes 3 conditions:
        if node.next == None:
            newnode = Node(node.count + 1)
            newnode.keys[key] = 0
            newnode.prev = node
            node.next = newnode
        elif node.next.count == node.count + 1:
            node.next.keys[key] = 0
        else:
            newnode = Node(node.count + 1)
            newnode.keys[key] = 0
            newnode.prev = node
            newnode.next = node.next
            node.next.prev = newnode
            node.next = newnode
        self.nodehash[key] = node.next
        if len(node.keys) == 0: self.remove(node)

    def get(self, key):

        if key not in self.valuehash:
            return -1
        self.increaseCount(key)
        return self.valuehash[key]

    def set(self, key, value):

        if self.cap == 0:
            return

        if key in self.valuehash:
            self.increaseCount(key)
        else:
            # when a new key emerges, we always need to removeOld first,
            # because if we don't, when the least frequent count > 1
            if len(self.valuehash) == self.cap:
                self.removeOld()
            self.addToHead(key)
        self.valuehash[key] = value



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)