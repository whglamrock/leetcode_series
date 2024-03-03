from collections import defaultdict, Counter
from copy import deepcopy
from math import sqrt
from typing import List, Dict

class Solution:
    def __init__(self):
        self.permutationCount = 0

    def numSquarefulPerms(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        numToSquarefulOther = defaultdict(set)
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.isSquarefulPair(nums[i], nums[j]):
                    numToSquarefulOther[nums[i]].add(nums[j])
                    numToSquarefulOther[nums[j]].add(nums[i])

        self.permutationCount = 0
        self.dfs([], numCount, numToSquarefulOther, len(nums))
        return self.permutationCount

    def dfs(self, currPermutation: List[int], numCount: Dict[int, int], numToSquarefulOther: Dict[int, set], n: int):
        if len(currPermutation) == n:
            self.permutationCount += 1
            return

        if not currPermutation:
            for num in numCount:
                nextNumCount = deepcopy(numCount)
                nextNumCount[num] -= 1
                if not nextNumCount[num]:
                    del nextNumCount[num]
                self.dfs([num], nextNumCount, numToSquarefulOther, n)
        else:
            num = currPermutation[-1]
            if num not in numToSquarefulOther:
                return
            for nextNum in numToSquarefulOther[num]:
                if nextNum not in numCount:
                    continue
                nextNumCount = deepcopy(numCount)
                nextNumCount[nextNum] -= 1
                if not nextNumCount[nextNum]:
                    del nextNumCount[nextNum]
                self.dfs(currPermutation + [nextNum], nextNumCount, numToSquarefulOther, n)

    def isSquarefulPair(self, num1: int, num2: int) -> bool:
        sqrtOf2 = sqrt(num1 + num2)
        return sqrtOf2 == int(sqrtOf2)


print(Solution().numSquarefulPerms([1, 17, 8]))
print(Solution().numSquarefulPerms([2, 2, 2]))
print(Solution().numSquarefulPerms([1, 1, 8, 1, 8]))
