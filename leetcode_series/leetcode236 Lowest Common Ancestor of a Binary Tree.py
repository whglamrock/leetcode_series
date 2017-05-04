
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


# iterative solution
# we always assume the p and q in the tree

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        if not root:
            return

        # remember in Python, the key could be a self-defined class and hashcode will calculated too
        parent = {root: None}
        # using stack to traverse the tree
        stack = [root]

        # the condition conjunction has to be "or" because the we need to find parent for both p and q
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
            ancestor.add(p)
            p = parent[p]
        while q not in ancestor:    # there is no need to check q is None
            q = parent[q]

        return q



'''
# common recursive solution

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        if not root:
            return

        # the recursion actually returns the lowestCommonAncestor of p or q
        # we only need one of (p, q) in the subtree without knowing it is specifically p or q
        def traversal(node, p, q):

            if node == p or node == q:
                return node
            leftans = helper(node.left, p, q) if node.left else None
            rightans = helper(node.right, p, q) if node.right else None
            if leftans and rightans:
                return node
            elif leftans:
                return leftans
            else:
                return rightans

        return traversal(root, p, q)
'''