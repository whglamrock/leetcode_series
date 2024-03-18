from collections import deque
from typing import List

# prefixSum & suffixSum + dp is the easiest idea to think of.
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefixSums = []
        for num in nums:
            if not prefixSums:
                prefixSums.append(num)
            else:
                prefixSums.append(num + prefixSums[-1])

        suffixSums = deque()
        for num in nums[::-1]:
            if not suffixSums:
                suffixSums.appendleft(num)
            else:
                suffixSums.appendleft(num + suffixSums[0])

        n = len(nums)
        # dp1[i] denotes the max sum with length of firstLen within nums[:i + 1]
        dp1 = [0] * n
        for i in range(firstLen - 1, n):
            subarraySum = prefixSums[i] - prefixSums[i - firstLen] if i >= firstLen else prefixSums[i]
            dp1[i] = max(dp1[i - 1], subarraySum)

        # dp2[i] denotes the max sum with length of secondLen within nums[:i + 1]
        dp2 = [0] * n
        for i in range(secondLen - 1, n):
            subarraySum = prefixSums[i] - prefixSums[i - secondLen] if i >= secondLen else prefixSums[i]
            dp2[i] = max(dp2[i - 1], subarraySum)

        # dp3[i] denotes the max suffix sum with length of firstLen within nums[i:]
        dp3 = [0] * n
        for i in range(n - firstLen, -1, -1):
            subarraySum = suffixSums[i] - suffixSums[i + firstLen] if i + firstLen < n else suffixSums[i]
            if i == n - 1:
                dp3[i] = subarraySum
            else:
                dp3[i] = max(dp3[i + 1], subarraySum)

        # dp4[i] denotes the max suffix sum with length of secondLen within nums[i:]
        dp4 = [0] * n
        for i in range(n - secondLen, -1, -1):
            subarraySum = suffixSums[i] - suffixSums[i + secondLen] if i + secondLen < n else suffixSums[i]
            if i == n - 1:
                dp4[i] = subarraySum
            else:
                dp4[i] = max(dp4[i + 1], subarraySum)

        maxSum = 0
        # putting firstLen first
        for i in range(n - 1):
            maxSum = max(maxSum, dp1[i] + dp4[i + 1])
        # putting secondLen first
        for i in range(n - 1):
            maxSum = max(maxSum, dp2[i] + dp3[i + 1])

        return maxSum
