from collections import OrderedDict

# You have to use OrderedDict if you wanna achieve O(1) for both get & put, in real interview.
class Node:
    def __init__(self, prev=None, next=None, count=None):
        self.prev = prev
        self.next = next
        self.count = count
        self.keys = OrderedDict()

class LFUCache:
    def __init__(self, capacity: int):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.keyToVal = {}
        self.keyToNode = {}
        self.capacity = capacity

    # it's assumed that the key is in the cache when this method is called
    def increaseCount(self, key: int):
        node = self.keyToNode[key]
        del node.keys[key]
        del self.keyToNode[key]

        count = node.count
        nextNode = node.next
        if nextNode.count == count + 1:
            nextNode.keys[key] = 0
            self.keyToNode[key] = nextNode
        else:
            newNode = Node(node, nextNode, count + 1)
            newNode.keys[key] = 0
            self.keyToNode[key] = newNode
            node.next, nextNode.prev = newNode, newNode

        if not node.keys:
            self.removeNode(node)

    # it's assumed that the key is not in the cache when this method is called
    def insertNewNode(self, key: int, val: int):
        self.keyToVal[key] = val
        firstNode = self.head.next

        if firstNode.count != 1:
            newNode = Node(self.head, firstNode, 1)
            self.head.next, firstNode.prev = newNode, newNode
            newNode.keys[key] = 0
            self.keyToNode[key] = newNode
        else:
            firstNode.keys[key] = 0
            self.keyToNode[key] = firstNode

    def popLeastFrequent(self):
        firstNode = self.head.next
        if firstNode == self.tail:
            return

        key, val = firstNode.keys.popitem(last=False)
        if not firstNode.keys:
            self.removeNode(firstNode)
        del self.keyToVal[key]
        del self.keyToNode[key]

    def removeNode(self, node: Node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        node.prev, node.next = None, None

    def get(self, key: int) -> int:
        if key not in self.keyToVal:
            return -1

        self.increaseCount(key)
        return self.keyToVal[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.keyToVal:
            if len(self.keyToVal) == self.capacity:
                self.popLeastFrequent()
            self.insertNewNode(key, value)
        else:
            self.increaseCount(key)
            self.keyToVal[key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
