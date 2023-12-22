from collections import OrderedDict


# to really achieve O(1) time for both get & put

class Node:
    def __init__(self, count):
        self.count = count
        self.prev, self.next = None, None
        self.keys = OrderedDict()


# using a dummy head and a dummy tail instead of solely initializing self.head = None can
# avoid all the key errors because we don't have to reset the head after adding a new node

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keyToVal = {}
        self.keyToNode = {}
        self.head, self.tail = Node(0), Node(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.cap = capacity

    # we assume when this method is called, the key is not in our cache
    def addNewKey(self, key, val):
        self.keyToVal[key] = val

        currFirstNode = self.head.next
        if currFirstNode.count == 1:
            # add the key to the count == 1 node
            currFirstNode.keys[key] = 0
            # add the key to the keyNode map
            self.keyToNode[key] = currFirstNode
        else:
            # create the node
            newFirstNode = Node(1)
            newFirstNode.keys[key] = 0
            # add the key to the keyNode map
            self.keyToNode[key] = newFirstNode
            # add the node to the linkedList
            newFirstNode.prev, newFirstNode.next = self.head, currFirstNode
            self.head.next, currFirstNode.prev = newFirstNode, newFirstNode

    # we assume when this method is called, the key is already in our cache
    def increaseCount(self, key):
        if key not in self.keyToVal:
            return

        node = self.keyToNode[key]
        # the key will point to a new node
        del node.keys[key]
        del self.keyToNode[key]

        nextNode = node.next
        if nextNode.count == node.count + 1:
            # add the key to count + 1's node
            nextNode.keys[key] = 0
            # add the node to the key node map
            self.keyToNode[key] = nextNode
        else:
            # create the new node
            newNode = Node(node.count + 1)
            newNode.keys[key] = 0
            # add the node to the key node map
            self.keyToNode[key] = newNode
            # add the new node to the linkedList
            newNode.prev, newNode.next = node, nextNode
            node.next, nextNode.prev = newNode, newNode

        if not node.keys:
            self.removeNode(node)

    def popLeastFrequent(self):
        firstNode = self.head.next
        # when there is no key to pop
        if firstNode.count == 0:
            return

        key, val = firstNode.keys.popitem(last=False)
        if not firstNode.keys:
            self.removeNode(firstNode)
        del self.keyToVal[key]
        del self.keyToNode[key]

    def removeNode(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        node.prev, node.next = None, None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyToVal:
            return -1
        self.increaseCount(key)
        return self.keyToVal[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cap == 0:  # stupid leetcode did give this corner case
            return

        if key in self.keyToVal:
            self.keyToVal[key] = value
            self.increaseCount(key)
        else:
            # do this before adding the key in keyToVal/keyToNode
            if len(self.keyToVal) == self.cap:
                self.popLeastFrequent()
            self.addNewKey(key, value)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
