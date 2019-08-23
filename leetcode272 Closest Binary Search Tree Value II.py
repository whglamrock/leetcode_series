
# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None



# in real interview, it's pretty hard to directly give out the O(logN) solution. The expectation would be write
    # the O(N) solution bug free, but give out ~O(logN) idea

# draw a BST on paper/board to understand why we keep 2 stacks of predecessors and successors, and how
    # we can get next bigger and next smaller

# It's not strictly O(logN) solution because getNextSuccessor & getNextPredecessor is not constant time,
    # but it's strictly < O(N) because in the k while loop each node will only be append/pop from pred/succ once

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []

        pred, succ = [], []
        self.initializePred(root, target, pred)
        self.initializeSucc(root, target, succ)

        # To avoid overlapping, we need to pop out one; we could also cut 1 from pred
        # It's BST so there won't be duplicate values. Thus we can use "is" check
        if pred and succ and pred[-1] is succ[-1]:
            self.getNextSuccessor(succ)

        ans = []

        while k:
            if pred and succ:
                diffToPred, diffToSucc = abs(target - pred[-1].val), abs(target - succ[-1].val)
                if diffToPred > diffToSucc:
                    ans.append(self.getNextSuccessor(succ))
                else:
                    ans.append(self.getNextPredecessor(pred))
            elif not pred:
                ans.append(self.getNextSuccessor(succ))
            elif not succ:
                ans.append(self.getNextPredecessor(pred))
            k -= 1

        return ans

    # store the nodes that are <= target along the path
    def initializePred(self, root, target, pred):
        while root:
            if root.val == target:
                pred.append(root)
                break
            if root.val > target:
                root = root.left
            else:
                pred.append(root)
                root = root.right

    # store the nodes that are >= target along the path
    def initializeSucc(self, root, target, succ):
        while root:
            if root.val == target:
                succ.append(root)
                break
            if root.val > target:
                succ.append(root)
                root = root.left
            else:
                root = root.right

    # the time complexity of this depends on whether the BST is a balanced tree
    def getNextPredecessor(self, pred):
        curr = pred.pop()
        res = curr.val
        curr = curr.left
        while curr:
            pred.append(curr)
            curr = curr.right
        return res

    # the time complexity of this depends on whether the BST is a balanced tree
    def getNextSuccessor(self, succ):
        curr = succ.pop()
        res = curr.val
        curr = curr.right
        while curr:
            succ.append(curr)
            curr = curr.left
        return res



'''
# easier to remember solution, but O(N)

class Solution(object):
    def closestKValues(self, root, target, k):

        if not root:
            return

        nums = []
        self.inOrder(root, nums)
        l, r = self.findTwoPointers(nums, target)

        ans = []
        # no need to special case for when l == -1 or r == len(nums)
        while k:
            if 0 <= l and r < len(nums):
                diffToLeft = abs(target - nums[l])
                diffToRight = abs(target - nums[r])
                if diffToLeft >= diffToRight:
                    ans.append(nums[r])
                    r += 1
                else:
                    ans.append(nums[l])
                    l -= 1
            elif l < 0:
                ans.append(nums[r])
                r += 1
            else:
                ans.append(nums[l])
                l -= 1
            k -= 1

        return ans

    def inOrder(self, root, traversal):
        if not root:
            return
        self.inOrder(root.left, traversal)
        traversal.append(root.val)
        self.inOrder(root.right, traversal)

    def findTwoPointers(self, nums, target):
        i = 0
        while i < len(nums) and nums[i] <= target:
            i += 1

        return i - 1, i
'''