from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# To avoid MLE in leetcode, simple level order traversal with redundant null values won't work, so we need to count
# the number of consecutive null nodes in the next level
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        todo = [root]
        maxWidth = 1
        while todo:
            nextTodo = []
            firstNonNullNode, lastNonNullNode = None, None
            numOfConsecutiveNullNodesInNext = 0
            currNumOfNodes = 0
            for node in todo:
                if type(node) == int:
                    currNumOfNodes += node
                    numOfConsecutiveNullNodesInNext += node * 2
                else:
                    if firstNonNullNode is None:
                        firstNonNullNode = currNumOfNodes
                    lastNonNullNode = currNumOfNodes
                    currNumOfNodes += 1
                    if node.left:
                        if numOfConsecutiveNullNodesInNext:
                            nextTodo.append(numOfConsecutiveNullNodesInNext)
                        numOfConsecutiveNullNodesInNext = 0
                        nextTodo.append(node.left)
                    else:
                        numOfConsecutiveNullNodesInNext += 1
                    if node.right:
                        if numOfConsecutiveNullNodesInNext:
                            nextTodo.append(numOfConsecutiveNullNodesInNext)
                        numOfConsecutiveNullNodesInNext = 0
                        nextTodo.append(node.right)
                    else:
                        numOfConsecutiveNullNodesInNext += 1
            if numOfConsecutiveNullNodesInNext:
                nextTodo.append(numOfConsecutiveNullNodesInNext)

            # all null nodes, so no next level
            if firstNonNullNode is None and lastNonNullNode is None:
                break
            if firstNonNullNode is not None and lastNonNullNode is not None and firstNonNullNode != lastNonNullNode:
                maxWidth = max(maxWidth, lastNonNullNode - firstNonNullNode + 1)
            todo = nextTodo

        return maxWidth
