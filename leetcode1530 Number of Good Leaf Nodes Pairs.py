class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity is O(N ^ 2). You can maybe reduce it to O(N * log(N)) by maintaining a sorted distancesToLeaf
# for each node but it's not necessary. O(N ^ 2) solution is way more than enough in real interview.
# Proof of O(N ^ 2) for a full binary tree, also assuming the distance limit is very big:
# 1) For each node, the number of leaf nodes is 2 ^ h (h is the height/distance to leaf of this node)
# 2) so the nested for loop (left distance & right distance for loop) causes 2 ^ h * 2 ^ h = 2 ^ (2 * h) = n ^ 2
# where n is the number of nodes in this subtree
# 3) Considering each node in the tree from root downwards, the total time is: n ^ 2 + (n / 2) ^ * 2 + (n / 4) ^ 2 * 4
# + ... = n ^ 2 + (n ^ 2) / 2 + (n ^ 2) / 4 + (n ^ 2) / 8 + ... = O(n ^ 2)
class Solution:
    def __init__(self):
        self.count = 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        self.dfs(root, distance)
        return self.count

    def dfs(self, node: TreeNode, distance: int):
        if not node:
            return []
        if not node.left and not node.right:
            return [1]

        distancesToLeafNodesInLeftChild = self.dfs(node.left, distance)
        distancesToLeafNodesInRightChild = self.dfs(node.right, distance)
        for leftDistance in distancesToLeafNodesInLeftChild:
            for rightDistance in distancesToLeafNodesInRightChild:
                if leftDistance + rightDistance <= distance:
                    self.count += 1

        distancesToLeaf = []
        for leftDistance in distancesToLeafNodesInLeftChild:
            if leftDistance + 1 < distance:
                distancesToLeaf.append(leftDistance + 1)
        for rightDistance in distancesToLeafNodesInRightChild:
            if rightDistance + 1 < distance:
                distancesToLeaf.append(rightDistance + 1)
        return distancesToLeaf
