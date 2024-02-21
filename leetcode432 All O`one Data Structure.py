
class Node:
    def __init__(self, count=None, keys=None, prev=None, next=None):
        self.count = count
        self.keys = keys if keys else set()
        self.next = next
        self.prev = prev

class AllOne:
    def __init__(self):
        self.keyToNode = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def removeNode(self, node: Node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        node.prev, node.next = None, None

    def inc(self, key: str) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.keys.discard(key)
            del self.keyToNode[key]
            nextNode = node.next
            currCount = node.count
            # need to create a newNode
            if currCount + 1 != nextNode.count:
                newNode = Node(currCount + 1, {key}, node, nextNode)
                node.next, nextNode.prev = newNode, newNode
                self.keyToNode[key] = newNode
            else:
                self.keyToNode[key] = nextNode
                nextNode.keys.add(key)

            if not node.keys:
                self.removeNode(node)
        else:
            nextNode = self.head.next
            if nextNode.count != 1:
                newNode = Node(1, {key}, self.head, nextNode)
                self.head.next, nextNode.prev = newNode, newNode
                self.keyToNode[key] = newNode
            else:
                nextNode.keys.add(key)
                self.keyToNode[key] = nextNode

    def dec(self, key: str) -> None:
        node = self.keyToNode[key]
        node.keys.discard(key)
        del self.keyToNode[key]
        prevNode = node.prev

        currCount = node.count
        # after decrease the count will be 0
        if currCount == 1:
            if not node.keys:
                self.removeNode(node)
            return

        # need to create a new node
        if currCount - 1 != prevNode.count:
            newNode = Node(currCount - 1, {key}, prevNode, node)
            prevNode.next, node.prev = newNode, newNode
            self.keyToNode[key] = newNode
        else:
            prevNode.keys.add(key)
            self.keyToNode[key] = prevNode

        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        for value in self.tail.prev.keys:
            return value
        return ''

    def getMinKey(self) -> str:
        for value in self.head.next.keys:
            return value
        return ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
