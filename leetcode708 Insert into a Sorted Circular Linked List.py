class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node

        prev, curr = head, head.next
        while curr != head:
            if prev.val <= insertVal <= curr.val:
                break
            if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                break
            prev = prev.next
            curr = curr.next

        prev.next = node
        node.next = curr
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


'''
# original solution
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode

        # find the smallestNode
        minNode = head
        minNodePrev = None
        while minNode.next.val >= minNode.val:
            minNodePrev = minNode
            minNode = minNode.next
            if minNode == head:
                break

        if minNode.next.val < minNode.val:
            minNodePrev = minNode
            minNode = minNode.next

        # find the first node >= insertVal
        curr = minNode
        prev = None
        while curr.val < insertVal:
            prev = curr
            curr = curr.next
            if curr == minNode:
                break

        newNode = Node(insertVal, curr)
        # prev = none means insertVal <= all values, then curr's prev is minNodePrev
        if not prev:
            minNodePrev.next = newNode
        else:
            prev.next = newNode

        return head
'''
