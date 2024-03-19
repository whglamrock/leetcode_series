class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

# the double linked list solution should satisfy the need in real interview
class MyHashMap(object):
    def __init__(self):
        self.map = [None] * 10000

    def put(self, key: int, value: int) -> None:
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
        while curr.next is not None:
            curr = curr.next
        newNode = ListNode(key, value)
        curr.next = newNode
        newNode.prev = curr

    def get(self, key: int) -> int:
        node = self.findNode(key)
        return node.value if node else -1

    def remove(self, key: int) -> None:
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
