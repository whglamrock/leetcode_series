from typing import List

# shouldn't be too hard to think of moving each number to its corresponding index (e.g., 5 should be in nums[5])
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # this guarantees that the nums has a 0, so that
        # we can check if nums[i] == i instead of nums[i] == i - 1
        nums.append(0)
        n = len(nums)

        for i, num in enumerate(nums):
            if num < 0 or num >= n:
                nums[i] = 0

        for i in range(n):
            if nums[i] == 0:
                continue
            while nums[i] != i:
                j = nums[i]
                # to avoid infinite loop
                if nums[j] == j:
                    break
                nums[i], nums[j] = nums[j], nums[i]

        for i in range(1, n):
            if nums[i] != i:
                return i

        return n


print(Solution().firstMissingPositive([-2, 3, 7, 8, 9, 11, 12]))
print(Solution().firstMissingPositive([0, 3]))
# test case like this is why we append 0 at first
print(Solution().firstMissingPositive([1]))
