from collections import deque
from typing import List

# scanning backwards, use a decreasing stack. If we encounter a nums[i] > stack[-1] we keep popping.
# Then the last popped value is the biggest in between (a good candidate for s3. P.S. s1 < s2 > s3 and s1 < s3).
class Solution(object):
    def find132pattern(self, nums: List[int]) -> bool:

        if not nums or len(nums) < 3:
            return False

        s3 = -2147483648
        stack = deque()

        # traverse the nums, the pointers points to s1
        for i in range(len(nums) - 1, -1, -1):
            # nums[i] < the popped s3, it must < stack[-1] (stack saves the candidate for s2)
            if nums[i] < s3:
                return True
            # then this nums[i] >= s3
            while stack and stack[0] < nums[i]:
                s3 = stack.popleft()
            stack.appendleft(nums[i])

        return False


print(Solution().find132pattern(nums=[1, 2, 3, 4]))
print(Solution().find132pattern(nums=[3, 1, 4, 2]))
print(Solution().find132pattern(nums=[-1, 3, 2, 0]))
print(Solution().find132pattern(nums=[1, 3, 2, 4, 5, 6, 7, 8, 9, 10]))
