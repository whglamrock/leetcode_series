from collections import OrderedDict


# You have to use OrderedDict if you wanna achieve O(1) for both get & put. Also, to practically come up with a
# solution and write test cases in 45 mins, you have to use OrderedDict library.
class Node:
    def __init__(self, prev=None, next=None, count=0):
        self.prev, self.next, self.count = prev, next, count
        self.keyValues = OrderedDict()


class LFUCache:
    def __init__(self, capacity: int):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.keyToNode = {}
        self.capacity = capacity

    # it's assumed that this node is not head or tail, and there is no keys in the node
    def removeNode(self, node: Node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        node.prev, node.next = None, None

    def increaseCount(self, key: int):
        node = self.keyToNode[key]
        value = node.keyValues[key]
        del self.keyToNode[key]
        del node.keyValues[key]

        nextNode = node.next
        if nextNode.count == node.count + 1:
            nextNode.keyValues[key] = value
            self.keyToNode[key] = nextNode
        else:
            newNode = Node(node, nextNode, node.count + 1)
            newNode.keyValues[key] = value
            self.keyToNode[key] = newNode
            node.next, nextNode.prev = newNode, newNode

        if not node.keyValues:
            self.removeNode(node)

    def popOutLeastFrequent(self):
        firstNode = self.head.next
        if firstNode == self.tail or not firstNode.keyValues:
            return

        keyToPop, value = firstNode.keyValues.popitem(last=False)
        del self.keyToNode[keyToPop]
        if not firstNode.keyValues:
            self.removeNode(firstNode)

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1

        node = self.keyToNode[key]
        value = node.keyValues[key]
        self.increaseCount(key)
        return value

    # it's assumed the key is not in the data structure when this method is called
    def addNewKey(self, key: int, value: int):
        firstNode = self.head.next
        if firstNode.count == 1:
            firstNode.keyValues[key] = value
            self.keyToNode[key] = firstNode
        else:
            newNode = Node(self.head, firstNode, 1)
            self.head.next, firstNode.prev = newNode, newNode
            newNode.keyValues[key] = value
            self.keyToNode[key] = newNode

    def put(self, key: int, value: int) -> None:
        if key not in self.keyToNode:
            if len(self.keyToNode) == self.capacity:
                self.popOutLeastFrequent()
            self.addNewKey(key, value)
        else:
            node = self.keyToNode[key]
            node.keyValues[key] = value
            self.increaseCount(key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
