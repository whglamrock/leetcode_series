
from collections import deque

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        ans = max(nums)  # P.S.: consider case when nums = [-2, -1]
        q = deque()
        currSum = 0

        # the strategy is that the sliding window won't start with a negative number;
            # so we need the initial ans = max(nums) to deal with the case where all nums < 0
        for num in nums:
            q.append(num)
            currSum += num
            while currSum < 0 and q:
                currSum -= q.popleft()
            if q:
                ans = max(ans, currSum)

        return ans



nums = [-2, -1, -1, -1, 7, 4, -3, -4, -5, 5]
Sol = Solution()
print Sol.maxSubArray(nums)
