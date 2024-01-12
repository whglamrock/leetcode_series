from typing import List

# find any prefixSum + suffixSum with no overlapping that equal to x
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        curr = 0
        prefixSumToIndex = {}
        for i, num in enumerate(nums):
            curr += num
            if curr not in prefixSumToIndex:
                # store the min index for the prefixSum
                prefixSumToIndex[curr] = i

        ans = 2147483647
        # not using any suffix
        if x in prefixSumToIndex:
            ans = prefixSumToIndex[x] + 1

        suffixSum = 0
        # at least use one suffix number
        for i in range(len(nums) - 1, -1, -1):
            suffixSum += nums[i]
            if suffixSum == x:
                ans = min(ans, len(nums) - i)
                continue
            if x - suffixSum in prefixSumToIndex and prefixSumToIndex[x - suffixSum] < i:
                ans = min(ans, prefixSumToIndex[x - suffixSum] + 1 + len(nums) - i)

        return ans if ans != 2147483647 else -1


print(Solution().minOperations([15, 2, 20, 1, 1, 3, 4], 9))
print(Solution().minOperations([3, 2, 20, 1, 1, 3], 10))
print(Solution().minOperations([5, 6, 7, 8, 9], 4))
print(Solution().minOperations([1, 1, 4, 2, 3], 5))
