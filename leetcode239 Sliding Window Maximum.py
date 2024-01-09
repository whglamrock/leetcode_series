
from collections import deque

# O(N) decreasing queue/stack solution
class Solution(object):
    def maxSlidingWindow(self, nums, k):

        window = deque()
        ans = []

        for i, num in enumerate(nums):
            # remove the elements out of the window
            while window and window[0] < i - k + 1:
                window.popleft()
            # the window is a decreasing queue because we don't care about the smaller elements in between
            while window and nums[window[-1]] <= num:
                window.pop()
            # add the current index to window
            window.append(i)
            # add max of window to ans
            if i >= k - 1:
                ans.append(nums[window[0]])

        return ans


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))