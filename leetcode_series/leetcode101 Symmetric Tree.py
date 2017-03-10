class Solution(object):  #iterative solution
    def isSymmetric(self, root):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack_for_tree1 = []
        stack_for_tree2 = []
        stack_for_tree1.append(root)
        stack_for_tree2.append(root)
        while stack_for_tree1 and stack_for_tree2:
            p1 = stack_for_tree1.pop()
            p2 = stack_for_tree2.pop()
            if (p1== None and p2 != None) or (p2== None and p1 != None):
                return False
            if p1== None and p2 == None:
                continue
            if p1.val != p2.val:
                return False

            stack_for_tree1.append(p1.left)
            stack_for_tree1.append(p1.right)

            stack_for_tree2.append(p2.right)
            stack_for_tree2.append(p2.left)

        return True
