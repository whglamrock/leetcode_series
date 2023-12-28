from collections import defaultdict
from typing import List, Dict

class Solution:
    def __init__(self):
        # use a non local variable for dfs/backtracking
        self.res = 0

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.res = 0
        nums.sort()
        numCount = defaultdict(int)
        self.dfs(nums, k, 0, numCount)

        # exclude the empty set. in the dfs logic, if we keep not using nums[i],
        # it will result in one empty set scenario
        return self.res - 1

    # dfs & backtracking
    def dfs(self, nums: List[int], k: int, i: int, numCount: Dict[int, int]):
        if i == len(nums):
            self.res += 1
            return
        num = nums[i]
        if numCount[num - k] == 0:
            numCount[num] += 1
            # do dfs with this number used for the subset
            self.dfs(nums, k, i + 1, numCount)
            numCount[num] -= 1

        # do dfs without this number used for the subset
        self.dfs(nums, k, i + 1, numCount)


print(Solution().beautifulSubsets(nums=[2, 4, 6], k=2))
print(Solution().beautifulSubsets(nums=[1], k=1))
print(Solution().beautifulSubsets(nums=[10, 4, 5, 7, 2, 1], k=3))


'''
# bruteforce backtrack solution that got TLE
from copy import deepcopy

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        indexesToValueSet = {}
        for i, num in enumerate(nums):
            indexesToValueSet[str(i)] = set([num])
        currNum = len(nums)
        return self.backtrack(nums, indexesToValueSet, currNum, k)

    def deserializeIndexesStr(self, indexesStr: str) -> List[int]:
        indexArrayInStr = indexesStr.split(',')
        return [int(item) for item in indexArrayInStr]

    def serializeIndexes(self, indexes: List[int]) -> str:
        indexesInStr = [str(item) for item in indexes]
        return ','.join(indexesInStr)

    def backtrack(self, nums: List[int], indexesToValueSet: Dict[list, set], currNum: int, k: int) -> int:
        n = len(nums)
        nextIndexesToValueSet = {}
        for indexesStr in indexesToValueSet:
            indexes = self.deserializeIndexesStr(indexesStr)
            i = indexes[-1]
            for j in range(i + 1, n):
                if nums[j] - k not in indexesToValueSet[indexesStr]:
                    newIndexes = indexes + [j]
                    newValueSet = deepcopy(indexesToValueSet[indexesStr])
                    newValueSet.add(nums[j])
                    nextIndexesToValueSet[self.serializeIndexes(newIndexes)] = newValueSet
        currNum += len(nextIndexesToValueSet)
        #print(nextIndexesToValueSet)
        #print(currNum)
        if nextIndexesToValueSet:
            return self.backtrack(nums, nextIndexesToValueSet, currNum, k)
        else:
            return currNum

'''
