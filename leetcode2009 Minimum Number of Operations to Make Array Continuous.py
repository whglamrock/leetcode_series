from typing import List

# To deal with duplicates:
# 1) each duplicate will need exactly one operation (e.g., 4,5,8,8,9,9 will need 2 operations for duplicates)
# 2) without removing duplicates, the only thing we are worrying about is the number of duplicates within the window
# 3) based on 2), we remove all duplicates, which takes out the number of operations within the window (duplicates) and
# outside the window ==> which doesn't affect the total number of operations.
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        l = 0
        numOfOperations = n - 1
        for r, num in enumerate(nums):
            while num - nums[l] > n - 1:
                l += 1
            numOfOperations = min(numOfOperations, n - (r - l + 1))

        return numOfOperations


print(Solution().minOperations(nums=[8, 5, 9, 9, 8, 4]))
print(Solution().minOperations(nums=[1, 10, 100, 1000]))
print(Solution().minOperations(nums=[1, 2, 3, 5, 6]))
print(Solution().minOperations(nums=[4, 2, 5, 3]))
