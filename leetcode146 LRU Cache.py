
# it's natural to think of orderedmap idea. No need for further explanation

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None



class OrderedMap:
    def __init__(self):
        self.keyToNode = {}
        self.head, self.tail = Node(None, None), Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head

    def size(self):
        return len(self.keyToNode)

    def get(self, key):
        if key not in self.keyToNode:
            return None
        else:
            val = self.keyToNode[key].val
            self.remove(key)
            self.put(key, val)
            return val

    def remove(self, key):
        if key not in self.keyToNode:
            return
        node = self.keyToNode[key]

        # remove from map
        del self.keyToNode[key]

        # remove from linkedlist
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        node.prev, node.next = None, None

    def put(self, key, val):
        if key in self.keyToNode:
            self.remove(key)

        # add to the map
        node = Node(key, val)
        self.keyToNode[key] = node

        # add the node
        prevFirstNode = self.head.next
        node.prev, node.next = self.head, prevFirstNode
        self.head.next, prevFirstNode.prev = node, node

    # pop the last node
    def pop(self):
        lastNode = self.tail.prev
        if lastNode.val == None:  # lastNode is actually head
            return
        self.remove(lastNode.key)



class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.orderedMap = OrderedMap()
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.orderedMap.get(key)
        return val if val != None else -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.orderedMap.put(key, value)
        while self.orderedMap.size() > self.cap:
            self.orderedMap.pop()



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

