
class ListNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev, self.next = prev, next


class LRUCache:
    def __init__(self, capacity: int):
        self.head, self.tail = ListNode(), ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.keyToNode = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1

        val = self.keyToNode[key].val
        self.deleteKey(key)
        self.put(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.deleteKey(key)
        else:
            if len(self.keyToNode) == self.capacity:
                lastKey = self.tail.prev.key
                # in this case, capacity is 0
                if lastKey is None:
                    return
                self.deleteKey(lastKey)

        self.addNewNode(key, value)

    def addNewNode(self, key: int, val: int) -> None:
        newNode = ListNode(key, val)
        firstNode = self.head.next
        self.head.next, firstNode.prev = newNode, newNode
        newNode.prev, newNode.next = self.head, firstNode
        self.keyToNode[key] = newNode

    def deleteKey(self, key: int) -> None:
        if key not in self.keyToNode:
            return

        node = self.keyToNode[key]
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        node.prev, node.next = None, None
        del self.keyToNode[key]

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
