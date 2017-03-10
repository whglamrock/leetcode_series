# the key is to understand the function of NestedInteger object.
# definition can be found from: https://leetcode.com/problems/nested-list-weight-sum/
class Solution(object):
    def depthSum(self, nestedList):

        if len(nestedList) == 0: return 0
        stack = []
        sum = 0
        for n in nestedList:
            stack.append((n, 1))  # depth = 1 for all big elements (e.g. nestedList = [1,[4,[6]]],
            # element 1, [4,[6]] is in depth 1)
        while stack:
            next, d = stack.pop(0) # pop from the first, because we append to the last.
            if next.isInteger():  # assume next = [4,[6]]
                sum += d * next.getInteger() # this element is an integer
            else:
                for i in next.getList():
                    stack.append((i,d+1)) # e.g. nestedList = [1,[4,[6]]], one round of this loop will
                    # change stack from [] to [(4,2),([6],2)]
        return sum

