from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        n = len(nums)
        smallest, largest = [2147483647] * n, [-2147483648] * n
        minSoFar = nums[0]
        for i, num in enumerate(nums):
            minSoFar = min(minSoFar, num)
            smallest[i] = minSoFar
        maxSoFar = nums[-1]
        for i in range(n - 1, -1, -1):
            maxSoFar = max(maxSoFar, nums[i])
            largest[i] = maxSoFar

        for i in range(1, n - 1):
            if smallest[i - 1] < nums[i] < largest[i + 1]:
                return True
        return False


print(Solution().increasingTriplet([9, 4, 3, 1, 6, 2, 8]))
print(Solution().increasingTriplet([1, 1, 1, 1]))
