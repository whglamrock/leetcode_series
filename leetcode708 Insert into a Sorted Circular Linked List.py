# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insert(self, head, insertVal):
        node = Node(insertVal)
        if not head:
            node.next = node
            return node

        prev, curr = head, head.next

        while prev.next != head:
            # Case1: 1 <- Node(2) <- 3
            if prev.val <= node.val <= curr.val:
                break

            # Case2: 3 -> 1, 3 -> Node(4) -> 1, 3 -> Node(0) -> 1
            if prev.val > curr.val and (node.val > prev.val or node.val < curr.val):
                break

            prev, curr = prev.next, curr.next

        node.next = curr
        prev.next = node

        return head


def buildTestNodes(nodeVals):
    head = None
    prev = None

    for val in nodeVals:
        node = Node(val)
        if prev:
            prev.next = node
        if not head:
            head = node

        prev = node

    prev.next = head
    return head


def printNodes(head):
    if head.next == head:
        print("nodes are: " + str(head.val))
        return

    curr = head
    vals = []
    while curr.next != head:
        vals.append(curr.val)
        curr = curr.next
    vals.append(curr.val)

    print("nodes are: " + str(vals))


node1 = buildTestNodes([3, 4, 1])
print(node1.val)
printNodes(Solution().insert(node1, 2))

node2 = buildTestNodes([1])
print(node2.val)
printNodes(Solution().insert(node2, 2))
