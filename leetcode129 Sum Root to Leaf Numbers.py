
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):

        if (not root):
            return 0

        stack = [[root,root.val]]
        while True:
            new = []
            counter = 0
            for item in stack:  # every item represents a unique path to the current level
                value = item.pop()
                if item[-1].left:   # the last element 'value' stores present number built from the root to current level
                    new.append(item+[item[-1].left,value*10+item[-1].left.val])
                    counter += 1
                if item[-1].right:
                    new.append(item+[item[-1].right,value*10+item[-1].right.val])
                    counter += 1
                if (not item[-1].left) and (not item[-1].right):
                    new.append(item+[value])
            stack = new
            if counter == 0:  # while there are no new nodes added
                break

        res = 0
        for item in stack:
            res += item[-1]  # sum up all values

        return res