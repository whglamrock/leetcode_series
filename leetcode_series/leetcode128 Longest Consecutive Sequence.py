
from collections import deque

class Solution(object):
    def longestConsecutive(self, nums):

        if not nums:
            return 0
        ans = 0
        nums = set(nums)

        while nums:
            # randomly choose a num and start the union find
            start = None
            for num in nums:
                start = num
                break
            # no need to check if the start is None, because the condition for while loop
            # initialize the start of the union
            nums.discard(start)
            union = deque([start])
            # keep unifying leftward
            while union[0] - 1 in nums:
                nums.discard(union[0] - 1)
                union.appendleft(union[0] - 1)
            # keep unifying rightward
            while union[-1] + 1 in nums:
                nums.discard(union[-1] + 1)
                union.append(union[-1] + 1)
            ans = max(ans, len(union))

        return ans



nums = [100,1,3,4,2,6,5,8]
a = Solution()
b = a.longestConsecutive(nums)
print b




