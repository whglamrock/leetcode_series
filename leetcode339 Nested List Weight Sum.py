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
# non recursion stack solution
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        stack = []
        for item in nestedList:
            stack.append([1, item])
        
        nestedSum = 0
        while stack:
            depth, item = stack.pop()
            if item.isInteger():
                nestedSum += depth * item.getInteger()
            else:
                for nestedItem in item.getList():
                    stack.append([depth + 1, nestedItem])
        
        return nestedSum
'''