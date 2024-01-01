from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        numOfOperations = 0
        # target stores the possibly biggest nums[i] in nums[i + 1:] (after breaking down any big number)
        target = nums[-1]

        # # we scan from right to left
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            if num <= target:
                target = num
                continue
            # in this case don't change the target
            if num % target == 0:
                numOfOperations += num // target - 1
            else:
                numOfElements = num // target + 1
                numOfOperations += num // target
                target = num // numOfElements

        return numOfOperations


print(Solution().minimumReplacement([1, 9, 5, 13, 7, 100, 27]))
print(Solution().minimumReplacement([3, 11, 3]))
print(Solution().minimumReplacement([1, 2, 3, 4, 5]))
