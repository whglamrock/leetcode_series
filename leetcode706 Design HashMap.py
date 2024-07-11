class ListNode:
    def __init__(self, key: int, value: int, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        self.keyToListNode = [ListNode(-1, -1) for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        head = self.keyToListNode[key % 10000]
        curr = head.next
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        firstNode = head.next
        newNode = ListNode(key, value)
        head.next = newNode
        newNode.next = firstNode

    def get(self, key: int) -> int:
        head = self.keyToListNode[key % 10000]
        curr = head.next
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        head = self.keyToListNode[key % 10000]

        # iterate the linkedList to find the node
        curr = head.next
        prev = head
        while curr:
            if curr.key == key:
                break
            prev = curr
            curr = curr.next

        if not curr:
            return

        # cut out the node
        nextNode = curr.next
        prev.next = nextNode
        curr.next = None
