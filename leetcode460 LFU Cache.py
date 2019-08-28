
from collections import OrderedDict

# using a dummy head and a dummy tail instead of solely initializing self.head = None can
#   avoid all the key errors because we don't have to reset the head after adding a new node

class Node:
    def __init__(self, count):
        self.count = count
        self.keys = OrderedDict()
        self.prev = None
        self.next = None



class LFUCache(object):
    def __init__(self, capacity):

        self.cap = capacity
        # separate the key-value pair hash from the linked list can save some trouble
        self.keytovalue = {}
        self.keytonode = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next, self.tail.prev = self.tail, self.head

    def addtoHead(self, key):
        oldfirstNode = self.head.next

        if oldfirstNode.count != 1:
            # create the new node
            newnode = Node(1)
            # connect it into the doubly-linked list
            newnode.prev, newnode.next = self.head, oldfirstNode
            self.head.next, oldfirstNode.prev = newnode, newnode
            # put the key into the new node's keys
            newnode.keys[key] = 0  # Python doesn't have OrderedSet
            self.keytonode[key] = newnode
        else:
            oldfirstNode.keys[key] = 0
            self.keytonode[key] = oldfirstNode

    def removetheNode(self, node):

        if node.count == 0:
            return

        prevnode, nextnode = node.prev, node.next
        node.prev, node.next = None, None
        if prevnode:  # very important to check if the prevnode is None
            prevnode.next = nextnode
        if nextnode:  # very important to check if the nextnode is None
            nextnode.prev = prevnode

    def removeLeastFrequent(self):

        leastFrequentNode = self.head.next
        if leastFrequentNode.count == 0:
            return

        # no need to check, because if it was empty, it would have been removed before
        key, val = leastFrequentNode.keys.popitem(last = False)
        if not leastFrequentNode.keys:
            self.removetheNode(leastFrequentNode)

        del self.keytonode[key]
        del self.keytovalue[key]

    # when this method is called, we assume key is in the cache
    def increaseCount(self, key):
        if key not in self.keytonode:
            return

        node = self.keytonode[key]
        # the key will point to a new node
        del self.keytonode[key]
        # remove the key from this node
        del node.keys[key]

        if node.next.count != node.count + 1:
            # create the node
            newnode = Node(node.count + 1)
            newnode.keys[key] = 0
            # add node to the linkedList
            nextnode = node.next
            newnode.prev, newnode.next = node, nextnode
            node.next = newnode
            nextnode.prev = newnode
        else:
            node.next.keys[key] = 0

        self.keytonode[key] = node.next

        if not node.keys:
            self.removetheNode(node)

    def get(self, key):

        if key not in self.keytovalue:
            return -1

        self.increaseCount(key)
        return self.keytovalue[key]

    def put(self, key, value):

        if self.cap == 0:  # leetcode did give this corner case
            return

        if key in self.keytovalue:
            self.increaseCount(key)
        else:
            # do this before adding the key in keyToVal/keyToNode
            if len(self.keytovalue) == self.cap:
                self.removeLeastFrequent()
            self.addtoHead(key)

        self.keytovalue[key] = value



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)