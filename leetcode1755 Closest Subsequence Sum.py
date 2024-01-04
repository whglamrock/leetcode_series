from typing import List

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        sumsOf1stHalf = set()
        self.dfsSearchToFindAllPossibleSums(nums[:len(nums) // 2], 0, 0, sumsOf1stHalf)
        sumsOf2ndHalf = set()
        self.dfsSearchToFindAllPossibleSums(nums[len(nums) // 2:], 0, 0, sumsOf2ndHalf)

        sumsOf2ndHalf = sorted(sumsOf2ndHalf)
        ans = 2147483647
        for s1 in sumsOf1stHalf:
            target = goal - s1
            i2 = self.findClosestIndex(sumsOf2ndHalf, target)
            if 0 <= i2 < len(sumsOf2ndHalf):
                ans = min(ans, abs(goal - (s1 + sumsOf2ndHalf[i2])))

        return ans

    def dfsSearchToFindAllPossibleSums(self, nums: List[int], i: int, currSum: int, possibleSums: set):
        if i == len(nums):
            possibleSums.add(currSum)
            return
        # don't use nums[i]
        self.dfsSearchToFindAllPossibleSums(nums, i + 1, currSum, possibleSums)
        # use nums[i]
        self.dfsSearchToFindAllPossibleSums(nums, i + 1, currSum + nums[i], possibleSums)

    def findClosestIndex(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            # in exit condition
            if l == r:
                if nums[l] == target:
                    return l
                if nums[l] > target and l > 0:
                    return l if abs(nums[l] - target) <= abs(nums[l - 1] - target) else l - 1
                if nums[l] < target and l + 1 < len(nums):
                    return l if abs(nums[l] - target) <= abs(nums[l + 1] - target) else l + 1
                return l
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        return l if l >= 0 else r


print(Solution().minAbsDifference(nums=[5, -7, 3, 5], goal=6))
print(Solution().minAbsDifference(nums=[7, -9, 15, -2], goal=-5))
print(Solution().minAbsDifference(nums=[1, 2, 3], goal=-7))
