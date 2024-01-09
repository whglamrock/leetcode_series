from typing import List

# one tricky idea we have to think of is: to break down any number into smaller targets, the absolute fastest
# approach will need (num // target or nm // target - 1) operations. Do not think in binary division direction!
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
                # small trick to build the new target: target = num // (num // target + 1)
                # e.g., consider num = 10 and target = 4. The new target needs to be 3
                numOfElements = num // target + 1
                numOfOperations += num // target
                target = num // numOfElements

        return numOfOperations


print(Solution().minimumReplacement([1, 9, 5, 13, 7, 100, 27]))
print(Solution().minimumReplacement([3, 11, 3]))
print(Solution().minimumReplacement([1, 2, 3, 4, 5]))
