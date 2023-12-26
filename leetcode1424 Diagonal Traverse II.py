from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        maxIndexSum = max(len(row) for row in nums) - 1 + len(nums) - 1
        indexSumToNums = defaultdict(list)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums[i])):
                indexSum = i + j
                indexSumToNums[indexSum].append(nums[i][j])

        output = []
        for indexSum in range(maxIndexSum + 1):
            if indexSum not in indexSumToNums:
                continue
            output += indexSumToNums[indexSum]

        return output


print(Solution().findDiagonalOrder(nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
print(Solution().findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
