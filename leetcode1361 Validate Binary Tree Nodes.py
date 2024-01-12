from typing import List

# It's not super difficult to realize that:
# 1) there should be exactly one node that has no parent
# 2) any node has more than 1 parent
# But, there is one edge case like: few nodes form a ring, and the rest form a valid binary tree.
# In this case we need to traverse tree and count nodes to see if it == n
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        nodeToParent = {}
        for i in range(n):
            # duplicate parent
            if (leftChild[i] != -1 and leftChild[i] in nodeToParent) or (
                    rightChild[i] != -1 and rightChild[i] in nodeToParent):
                return False
            nodeToParent[leftChild[i]] = i
            nodeToParent[rightChild[i]] = i

        nodeWithNoParent = set()
        for i in range(n):
            if i not in nodeToParent:
                nodeWithNoParent.add(i)

        # possible ring situation
        if len(nodeWithNoParent) != 1:
            return False

        # for the only possible root. do tree traversal
        todo = list(nodeWithNoParent)
        count = 0
        while todo:
            nextTodo = set()
            for node in todo:
                count += 1
                if leftChild[node] != -1:
                    nextTodo.add(leftChild[node])
                if rightChild[node] != -1:
                    nextTodo.add(rightChild[node])
            todo = nextTodo

        return count == n


