class ListNode:
    def __init__(self, count=None, keys=None, prev=None, next=None):
        self.count = count if count is not None else 0
        self.keys = keys if keys else set()
        self.prev, self.next = prev, next


# keep in mind that in python: in scenario like in line 62 you need to always do "prevNext = prevNode.next" instead of
# doing "newNode.prev, newNode.next = prevNode, prevNode.next; prevNode.next, prevNode.next.prev = newNode, newNode".
# otherwise the python's copy mechanism will give you some bullshit result
class AllOne:
    def __init__(self):
        self.head, self.tail = ListNode(), ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.keyToNode = {}

    def inc(self, key: str) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            nextNode = node.next
            node.keys.discard(key)
            currCount = node.count
            del self.keyToNode[key]

            if nextNode.count == currCount + 1:
                nextNode.keys.add(key)
                self.keyToNode[key] = nextNode
            else:
                newNode = ListNode(currCount + 1, {key})
                newNode.prev, newNode.next = node, nextNode
                node.next, nextNode.prev = newNode, newNode
                self.keyToNode[key] = newNode

            if not node.keys:
                self.removeNode(node)
        else:
            firstNode = self.head.next
            if firstNode.count != 1:
                newNode = ListNode(1, {key})
                self.keyToNode[key] = newNode
                newNode.prev, newNode.next = self.head, firstNode
                self.head.next, firstNode.prev = newNode, newNode
            else:
                firstNode.keys.add(key)
                self.keyToNode[key] = firstNode

    def dec(self, key: str) -> None:
        node = self.keyToNode[key]
        currCount = node.count
        node.keys.discard(key)
        del self.keyToNode[key]
        prevNode = node.prev
        if not node.keys:
            self.removeNode(node)

        if currCount == 1:
            return

        if prevNode.count == currCount - 1:
            prevNode.keys.add(key)
            self.keyToNode[key] = prevNode
        else:
            newNode = ListNode(currCount - 1, {key})
            prevNext = prevNode.next
            newNode.prev, newNode.next = prevNode, prevNext
            prevNode.next, prevNext.prev = newNode, newNode
            self.keyToNode[key] = newNode

    def getMaxKey(self) -> str:
        for key in self.tail.prev.keys:
            return key
        return ''

    def getMinKey(self) -> str:
        for key in self.head.next.keys:
            return key
        return ''

    # it's assumed that this node is not head or tail
    def removeNode(self, node: ListNode):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        node.prev, node.next = None, None


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
