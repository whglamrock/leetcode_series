# the key finding is that for valid serialization, every number is followed by two "#"s or
# one number and a "#" or two numbers.

# A number followed by two '#'s represents a leaf and can be combined into a "#":
# e.g., in "9,3,4,#,#,1,#,#,2,#,6,#,#", '6,#,#' can be combined into a '#', and then with
# previous '2,#' be combined into a '#', so on and so forth.

class Solution(object):
    def isValidSerialization(self, preorder):

        if not preorder:
            return False

        stack = []
        preorder = preorder.split(',')
        for i in xrange(len(preorder) - 1, -1, -1):
            if preorder[i] != '#':
                if not stack or len(stack) < 2:
                    return False
                leaf1 = stack.pop()
                leaf2 = stack.pop()
                if leaf1 != '#' or leaf2 != '#':
                    return False
            stack.append('#')

        return len(stack) == 1