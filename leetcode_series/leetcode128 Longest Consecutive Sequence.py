
from collections import deque
class Solution(object):
    def longestConsecutive(self, nums):

        if not nums: return 0
        numset = set(nums)
        length = 0

        while numset:
            s = None
            for e in numset:
                s = e
                break
            if s == None: break
            curlen = 1
            todo = deque()
            todo.append(s)
            numset.discard(s)
            while True:
                prelen = len(todo)
                if todo[0] - 1 in numset:
                    newleft = todo[0] - 1
                    numset.discard(newleft)
                    todo.appendleft(newleft)
                    curlen += 1
                if todo[-1] + 1 in numset:
                    newright = todo[-1] + 1
                    numset.discard(newright)
                    todo.append(newright)
                    curlen += 1
                if len(todo) == prelen: break
            length = max(curlen, length)

        return length



nums = [100,1,3,4,2,6,5,8]
a = Solution()
b = a.longestConsecutive(nums)
print b




