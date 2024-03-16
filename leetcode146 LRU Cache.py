class Node:
    def __init__(self, key=None, val=None, nextNode=None, prevNode=None):
        self.key = key
        self.val = val
        self.next = nextNode
        self.prev = prevNode

class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keyToNode = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        # remove the node
        node = self.keyToNode[key]
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        # move the node to right after the head
        headNext = self.head.next
        self.head.next, headNext.prev = node, node
        node.prev, node.next = self.head, headNext
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.val = value
            prevNode, nextNode = node.prev, node.next
            prevNode.next, nextNode.prev = nextNode, prevNode
            node.prev, node.next = None, None
        else:
            # pop out the least recent node
            while self.capacity <= len(self.keyToNode):
                leastRecentNode = self.tail.prev
                leastRecentNodePrev = leastRecentNode.prev
                leastRecentNodePrev.next, self.tail.prev = self.tail, leastRecentNodePrev
                leastRecentNode.prev, leastRecentNode.next = None, None
                del self.keyToNode[leastRecentNode.key]
            # build the newNode
            node = Node(key, value)
            self.keyToNode[key] = node

        headNext = self.head.next
        self.head.next, headNext.prev = node, node
        node.prev, node.next = self.head, headNext

    def printLinkedList(self):
        curr = self.head.next
        ans = []
        while curr.key is not None:
            ans.append([curr.key, curr.val])
            curr = curr.next
        print(ans)


Sol = LRUCache(2)
Sol.put(2, 1241)
Sol.put(3, 13)
Sol.put(4, 124)
print(Sol.get(3))
print(Sol.get(2))
Sol.put(5, 314)
