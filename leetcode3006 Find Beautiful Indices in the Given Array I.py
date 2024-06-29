from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        matchedIndexesOfA = self.findMatchedIndexes(s, a)
        matchedIndexesOfB = sorted(self.findMatchedIndexes(s, b))

        ans = []
        for indexOfA in matchedIndexesOfA:
            closestSmallerIndexOfB = self.findClosestSmallerOrEqual(matchedIndexesOfB, indexOfA)
            closestBiggerIndexOfB = self.findClosestBiggerOrEqual(matchedIndexesOfB, indexOfA)
            if (closestSmallerIndexOfB != -1 and abs(closestSmallerIndexOfB - indexOfA) <= k) \
                    or (closestBiggerIndexOfB != -1 and abs(closestBiggerIndexOfB - indexOfA) <= k):
                ans.append(indexOfA)

        return sorted(ans)

    def findClosestSmallerOrEqual(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if nums[m] <= target:
                    return nums[m]
                return -1
            if nums[m] > target:
                r = m - 1
            else:
                l = m

        return -1

    def findClosestBiggerOrEqual(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] >= target:
                    return nums[m]
                return -1
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return -1

    def findMatchedIndexes(self, s: str, substr: str) -> List[int]:
        matchedIndexes = []
        for i in range(len(s) - len(substr) + 1):
            if s[i:i + len(substr)] == substr:
                matchedIndexes.append(i)

        return matchedIndexes
