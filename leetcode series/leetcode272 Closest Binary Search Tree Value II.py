
# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# idea is to keep two stacks of predecessors and successors

class Solution(object):

    def closestKValues(self, root, target, k):

        res, succ, pred = [], [], []
        self.initializePredecessorStack(root, target, pred)
        self.initializeSuccessorStack(root, target, succ)

        # to avoid overlapping, we need to pop out one;
        #   it could also be self.getNextSuccessor(succ).
        if succ and pred and succ[-1].val == pred[-1].val:  # important to check if succ/pred empty
            self.getNextPredecessor(pred)

        # since k will always <= n, we don't need to worry about when
        #   both succ and pred stack are empty
        while k > 0:
            if not pred:
                res.append(self.getNextSuccessor(succ))
            elif not succ:
                res.append(self.getNextPredecessor(pred))
            else:
                succ_diff = abs(float(succ[-1].val) - target)
                pred_diff = abs(float(pred[-1].val) - target)
                if succ_diff < pred_diff:
                    res.append(self.getNextSuccessor(succ))
                else:
                    res.append(self.getNextPredecessor(pred))
            k -= 1

        return res

    def initializePredecessorStack(self, root, target, pred):

        while root:
            if root.val == target:
                pred.append(root)
                break
            # then we need to go to the right subtree to find the target
            elif root.val < target:
                pred.append(root)
                root = root.right
            else:
                root = root.left

    def initializeSuccessorStack(self, root, target, succ):

        while root:
            if root.val == target:
                succ.append(root)
                break
            # then we need to go to the left subtree to find the target
            elif root.val > target:
                succ.append(root)
                root = root.left
            else:
                root = root.right

    def getNextPredecessor(self, pred):

        curr = pred.pop()
        res = curr.val
        curr = curr.left
        while curr:
            pred.append(curr)
            curr = curr.right

        return res

    def getNextSuccessor(self, succ):

        curr = succ.pop()
        res = curr.val
        curr = curr.right
        while curr:
            succ.append(curr)
            curr = curr.left

        return res