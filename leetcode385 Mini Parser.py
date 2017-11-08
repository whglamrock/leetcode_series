
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""

class NestedInteger(object):
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


# go through the case when s == "[123,[456,[789]],[[234]],345]"
class Solution(object):
    def deserialize(self, s):

        if (not s):
            return
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        curr = None
        l = 0

        for r in xrange(len(s)):
            if s[r] == '[':  # then we needa open a new curr, but before that we have to save the old curr to stack
                if curr != None:  # only to avoid in the first loop, because after that even curr = [],
                    # curr is not 'None' anymore.
                    stack.append(curr)
                curr = NestedInteger()
                l = r + 1
            elif s[r] == ',':  # when a num needs to end if it is an integer... however, curr doesn't necessarily
                # end, for there could be two or more consecutive integers.
                if s[r - 1] != ']':  # it is an integer. if not, we just move on to next r.
                    num = s[l:r]
                    curr.add(int(num))
                l = r + 1
            elif s[r] == ']':  # when we need to end a curr.
                num = s[l:r]
                if num != '':   # to avoid when there are two consecutive ']'s.
                    curr.add(int(num))
                if stack:   # the following three moves ensure we don't mess up the different depths.
                    popped = stack.pop()
                    popped.add(curr)  # curr could be '[]' because in our case the element [[234]] exists.
                    curr = popped
                l = r + 1

        return curr

