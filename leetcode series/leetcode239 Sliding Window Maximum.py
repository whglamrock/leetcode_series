# O(N) solution because every element will at most
# be put into and popped out once, respectively.
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = deque()
        ans = []
        # the size of queue within k;
        # the distance between the indices of the first and last element within k
        for i, num in enumerate(nums):
            while queue and queue[0] < i - k + 1:
                queue.popleft()
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans