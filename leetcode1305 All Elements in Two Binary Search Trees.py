from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1, list2 = [], []
        self.traverseTree(root1, list1)
        self.traverseTree(root2, list2)

        ans = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                ans.append(list1[i])
                i += 1
            else:
                ans.append(list2[j])
                j += 1
        if i < len(list1):
            ans += list1[i:]
        if j < len(list2):
            ans += list2[j:]

        return ans

    def traverseTree(self, node: TreeNode, valList: List[int]):
        if not node:
            return
        if node.left:
            self.traverseTree(node.left, valList)
        valList.append(node.val)
        if node.right:
            self.traverseTree(node.right, valList)
