
from collections import OrderedDict

# in the doubly linked list, the node (each node represents the keys with same count)
#   is sorted in ascending order

class Node:
    def __init__(self, count):

        self.count = count
        self.container = OrderedDict()
        self.prev = None
        self.next = None


class LFUCache(object):

    def __init__(self, capacity):

        self.cap = capacity
        # separate the key-value pair hash from the linked list can save lots of trouble
        self.valuehash = {}
        # a single node has a container that stores the keys with same count
        self.nodehash = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next, self.tail.prev = self.tail, self.head

    # need to consider two conditions; always put the mapping operation at the end
    def addtoHead(self, key):

        oldfirstnode = self.head.next
        # no matter if it's the case that we only have head & tail, or the case
        #   we only lack the node with count == 1, we have to create a new node
        if oldfirstnode.count != 1:
            # create the new node
            newnode = Node(1)
            # connect it into the doubly-linked list
            newnode.prev, newnode.next = self.head, oldfirstnode
            self.head.next, oldfirstnode.prev = newnode, newnode
            # put the key into the new node's container
            newnode.container[key] = 0   # or it can = anything, Python doesn't have OrderedSet
            # always put the hash alternation at last
            self.nodehash[key] = newnode
        else:
            oldfirstnode.container[key] = 0
            # always put the hash alternation at last
            self.nodehash[key] = oldfirstnode

    # simply remove the node; very important to remember to check if the node is None
    def removetheNode(self, node):

        prevnode, nextnode = node.prev, node.next
        if node.count == 0:
            return
        node.prev, node.next = None, None
        if prevnode:    # very important to check if the prevnode is None
            prevnode.next = nextnode
        if nextnode:    # very important to check if the nextnode is None
            nextnode.prev = prevnode

    # the least frequent key is stored in the first node
    def removetheLeastFrequent(self):

        firstnode = self.head.next
        if firstnode.count == 0:
            return

        # no need to check, because if it was empty, it would have been removed before
        key, val = firstnode.container.popitem(last = False)
        if len(firstnode.container) == 0:
            self.removetheNode(firstnode)

        if key in self.nodehash:    # very important to check the key error
            del self.nodehash[key]
        if key in self.valuehash:   # very important to check the key error
            del self.valuehash[key]

    def increaseCount(self, key):

        node = self.nodehash[key]
        del node.container[key]  # the hash delete job needs to be done first

        # remember to check whether the node.next == None
        if not node.next or node.next.count != node.count + 1:
            newnode = Node(node.count + 1)
            newnode.container[key] = 0
            nextnode = node.next
            newnode.prev, newnode.next = node, nextnode
            node.next = newnode
            if nextnode:    # very important to check if the nextnode is None
                nextnode.prev = newnode
        else:
            node.next.container[key] = 0

        self.nodehash[key] = node.next  # at this point, the node.next can't be None
        if len(node.container) == 0:
            self.removetheNode(node)

    def get(self, key):

        if key not in self.valuehash:
            return -1
        # the increase count operation won't change the key-value pair in valuehash
        self.increaseCount(key)
        # separate the key-value pair from the increaseCount process to avoid key error
        return self.valuehash[key]

    def put(self, key, value):

        if self.cap == 0:   # can't possibly happen, but just in case...
            return

        if key in self.valuehash:
            self.increaseCount(key)
        else:
            # remove a node first to make one spot available
            if len(self.valuehash) == self.cap:
                self.removetheLeastFrequent()
            self.addtoHead(key)
        # always put the hash alternation at last
        self.valuehash[key] = value



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)