
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# Most important point: we need to realize the max binary tree can be constructed with the certain rule
    # simply just iterating the nums from left to right
# we only need to know/keep track of the nodes on the right path of the tree
# see explanation in comment of: https://leetcode.com/problems/maximum-binary-tree/discuss/106156/Java-worst-case-O(N)-solution

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        stack = []
        for num in nums:
            curr = TreeNode(num)
            # at this point, we don't care any number in the stack because there are on the left of current num
            while stack and stack[-1].val < num:
                curr.left = stack.pop()
            # at this point, stack[-1].val > num
            if stack:
                stack[-1].right = curr
            stack.append(curr)

        # the number on the left of the stack will be the biggest
        return stack[0]