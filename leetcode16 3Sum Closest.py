from typing import List

# O(n ^ 2) time. idea came from 3sum
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff = 2147483647
        closestThreeSum = 0
        for i in range(2, len(nums)):
            l, r = 0, i - 1
            while l < r:
                threeSum = nums[l] + nums[r] + nums[i]
                if threeSum == target:
                    return threeSum
                diff = abs(threeSum - target)
                if diff < minDiff:
                    minDiff = diff
                    closestThreeSum = threeSum
                if threeSum < target:
                    l += 1
                else:
                    r -= 1

        return closestThreeSum
