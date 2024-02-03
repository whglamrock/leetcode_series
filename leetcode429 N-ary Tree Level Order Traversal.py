from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        ans = []
        todo = [root]
        while todo:
            nextTodo = []
            level = []
            for node in todo:
                level.append(node.val)
                if node.children:
                    nextTodo += node.children
            todo = nextTodo
            ans.append(level)
        return ans
