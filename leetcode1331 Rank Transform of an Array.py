from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(set(arr))
        numToRank = {}
        for i, num in enumerate(sortedArr):
            numToRank[num] = i + 1

        for i in range(len(arr)):
            num = arr[i]
            arr[i] = numToRank[num]

        return arr


print(Solution().arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]))
