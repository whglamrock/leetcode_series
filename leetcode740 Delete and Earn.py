from collections import Counter
from typing import List

# O(n) solution without sorting. With sorting it actually runs faster in leetcode
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        numsCount = Counter(nums)
        maxNum = max(numsCount.keys())
        take, skip = 0, 0
        # nums[i] is within 10^4
        prevNum = None
        for num in range(maxNum + 1):
            if num not in numsCount:
                continue
            if prevNum and prevNum == num - 1:
                takeNum = skip + num * numsCount[num]
            else:
                takeNum = max(take, skip) + num * numsCount[num]
            skipNum = max(skip, take)
            take, skip = takeNum, skipNum
            prevNum = num

        return max(take, skip)


print(Solution().deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
print(Solution().deleteAndEarn(nums=[3, 4, 2]))
