from heapq import *
from typing import List

# the stupid leetcode only accepts priorityQueue solution. cached DFS gets TLE.
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(list(zip(nums1, nums2)), key=lambda x: -x[1])
        pq = []
        prefixSum = 0
        ans = 0
        for num1, num2 in nums:
            prefixSum += num1
            heappush(pq, num1)
            if len(pq) == k:
                ans = max(ans, prefixSum * num2)
                prefixSum -= heappop(pq)

        return ans


'''
# original dfs solution that got TLE
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        self.nums1 = nums1
        self.nums2 = nums2
        return self.dfs(0, 0, 2147483648, k)
    
    @lru_cache(None)
    def dfs(self, i: int, currSum: int, currMin: int, k: int):
        if k == 0:
            return currSum * currMin
        # we won't be able to pick k numbers
        if i >= len(self.nums1):
            return -1

        maximumScore = -2147483648
        for j in range(i, len(self.nums1)):
            nextMin = min(currMin, self.nums2[j])
            maximumScore = max(maximumScore, self.dfs(j + 1, currSum + self.nums1[j], nextMin, k - 1))
        
        return maximumScore
'''