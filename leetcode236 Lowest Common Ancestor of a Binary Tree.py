
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# it's more realistic to think of this recursive solution in real interview

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # we only need to look for one of them because p, q are guaranteed both in the tree
        if root == p or root == q:
            return root

        # if p, q both not in leftAns the most inner recursion will hit condition "root.left == None"
        leftAns = self.lowestCommonAncestor(root.left, p, q) if root.left else None
        rightAns = self.lowestCommonAncestor(root.right, p, q) if root.right else None

        if leftAns and rightAns:
            return root
        elif leftAns:
            return leftAns
        else:
            return rightAns



'''
# iterative solution

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        if not root:
            return

        parent = {root: None}
        # using stack to traverse the tree (right subtree first DFS)
        stack = [root]

        # the condition conjunction has to be "or" because the we need both p and q
        while p not in parent or q not in parent:
            # there is no need to check the stack, because we always assume the p/q is in the tree
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # save all ancestors of p, and starting from q and going up to find the first one in ancestor
        ancestor = set()
        # it applies even when root == p or root == q
        while p:
            # don't add parent[p] here, think about that p is p's ancestor too
            ancestor.add(p)  # if parent[p] == None, adding parent[p] will add None
            p = parent[p]
        while q not in ancestor:    # there is no need to check q is None
            q = parent[q]

        return q
'''