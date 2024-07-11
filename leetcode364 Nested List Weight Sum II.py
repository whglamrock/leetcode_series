from typing import List


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
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


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        stack = []
        for item in nestedList:
            stack.append([1, item])

        valsWithDepths = []
        maxDepth = 1
        while stack:
            depth, item = stack.pop()
            if item.isInteger():
                valsWithDepths.append([item.getInteger(), depth])
            else:
                for subItem in item.getList():
                    stack.append([depth + 1, subItem])
            maxDepth = max(maxDepth, depth)

        ans = 0
        for val, depth in valsWithDepths:
            ans += (maxDepth - depth + 1) * val

        return ans
