from typing import List, Optional

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
    def __init__(self, value=None):
        pass

    def isInteger(self) -> bool:
        pass

    def add(self, elem):
        pass

    def setInteger(self, value):
        pass

    def getInteger(self) -> int:
        pass

    def getList(self) -> Optional[List['NestedInteger']]:
        pass

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.getSumWithDepth(nestedList, 1)

    def getSumWithDepth(self, nestedList: List[NestedInteger], depth: int) -> int:
        nestedSum = 0
        for nestedInt in nestedList:
            if nestedInt.isInteger():
                nestedSum += nestedInt.getInteger() * depth
            else:
                nestedSum += self.getSumWithDepth(nestedInt.getList(), depth + 1)

        return nestedSum


'''
# original non recursion stack solution
class Solution(object):
    def depthSum(self, nestedList):

        if len(nestedList) == 0:
            return 0
        stack = []
        nestedSum = 0
        for n in nestedList:
            stack.append((n, 1))  # depth = 1 for all big elements (e.g. nestedList = [1,[4,[6]]],
            # element 1, [4,[6]] is in depth 1)
        while stack:
            next, d = stack.pop(0)  # pop from the first, because we append to the last.
            if next.isInteger():  # assume next = [4,[6]]
                nestedSum += d * next.getInteger()  # this element is an integer
            else:
                for i in next.getList():
                    stack.append((i, d + 1))  # e.g. nestedList = [1,[4,[6]]], one round of this loop will
                    # change stack from [] to [(4,2),([6],2)]
        return nestedSum
'''
