from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsSet = set()
        numsWithoutDup = []
        for num in nums:
            if num not in numsSet:
                numsSet.add(num)
                numsWithoutDup.append(num)

        for i in range(len(numsWithoutDup)):
            nums[i] = numsWithoutDup[i]

        return len(numsWithoutDup)


nums = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(nums))
print(nums)
