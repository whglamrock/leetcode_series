from typing import List

# To deal with duplicates:
# 1) each duplicate will need exactly one operation (e.g., 4,5,8,8,9,9 will need 2 operations for duplicates)
# 2) without removing duplicates, the only thing we are worrying about is the number of duplicates within the window
# 3) based on 2), we remove all duplicates, which takes out the number of operations within the window (duplicates) and
# outside the window ==> which doesn't affect the total number of operations.
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        k = n - 1
        nums = sorted(set(nums))

        minNumOfOperations = k
        # for each num, the window is [num, num + k] inclusive. we find number of bigger & smaller elements
        for i, num in enumerate(nums):
            target = num + k
            if i < len(nums) - 1:
                indexOfBigger = self.findIndexBiggerThan(nums, i + 1, len(nums) - 1, target)
            else:
                indexOfBigger = len(nums)

            numOfBiggerNums = len(nums) - indexOfBigger
            numOfSmallerNums = i
            minNumOfOperations = min(minNumOfOperations, numOfBiggerNums + numOfSmallerNums)

        return minNumOfOperations + (n - len(nums))

    def findIndexBiggerThan(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            m = (l + r) // 2
            if l == r:
                # all numbers are <= target
                if nums[m] <= target:
                    # usually we return -1 but for this question we tailor made the return value
                    return len(nums)
                else:
                    return m

            if nums[m] > target:
                r = m
            else:
                l = m + 1

        return len(nums)


print(Solution().minOperations(nums=[8, 5, 9, 9, 8, 4]))
print(Solution().minOperations(nums=[1, 10, 100, 1000]))
print(Solution().minOperations(nums=[1, 2, 3, 5, 6]))
print(Solution().minOperations(nums=[4, 2, 5, 3]))
