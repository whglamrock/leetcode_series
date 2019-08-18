
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None



class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [None for _ in xrange(10000)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hashValue = self.hashCode(key)

        # not even a single value exists
        if not self.map[hashValue]:
            self.map[hashValue] = ListNode(key, value)
            return

        # update the value
        node = self.findNode(key)
        if node:
            node.value = value
            return

        # node doesn't exist but there is collision
        curr = self.map[hashValue]
        while curr.next != None:
            curr = curr.next
        newNode = ListNode(key, value)
        curr.next = newNode
        newNode.prev = curr

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        node = self.findNode(key)
        return node.value if node else -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        node = self.findNode(key)
        if not node:
            return

        hashValue = self.hashCode(key)
        # update the self.map[hashValue] when node is the head of the linked list
        if node == self.map[hashValue]:
            self.map[hashValue] = node.next

        # disconnect the prev and next
        prevNode, nextNode = node.prev, node.next
        if prevNode:
            prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode

    def hashCode(self, key):
        hashValue = key / 100
        return hashValue if hashValue < 10000 else 9999

    def findNode(self, key):
        hashValue = self.hashCode(key)

        if not self.map[hashValue]:
            return None

        curr = self.map[hashValue]
        while curr and curr.key != key:
            curr = curr.next
        return curr



hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print hashMap.get(1)
print hashMap.get(3)
print hashMap.get(2)
hashMap.put(2, 1)
print hashMap.get(2)
hashMap.remove(2)
print hashMap.get(2)