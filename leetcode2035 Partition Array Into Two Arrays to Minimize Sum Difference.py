from collections import defaultdict
from itertools import combinations
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        leftHalf, rightHalf = nums[:n], nums[n:]
        leftPossibleSums, rightPossibleSums = self.buildPossibleSums(leftHalf), self.buildPossibleSums(rightHalf)

        # init the variable ans by choosing all numbers from the arbitrary left half to form the final left and vice versa.
        ans = abs(sum(leftHalf) - sum(rightHalf))
        totalSum = sum(nums)
        halfSum = totalSum // 2

        # choose i numbers from the left half and n - i numbers from the right half
        # i can be from 1 to n - 1
        for i in range(1, n):
            leftSums = leftPossibleSums[i]
            rightSums = rightPossibleSums[n - i]
            rightSums = sorted(rightSums)
            for leftSum in leftSums:
                target = halfSum - leftSum
                j = self.findClosestIndex(rightSums, target)
                diff = abs((leftSum + rightSums[j]) - (totalSum - leftSum - rightSums[j]))
                ans = min(ans, diff)

        return ans

    def buildPossibleSums(sellf, nums: List[int]):
        possibleSums = defaultdict(set)
        for i in range(1, len(nums) + 1):
            for combination in combinations(nums, i):
                possibleSums[i].add(sum(combination))
        return possibleSums

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


print(Solution().minimumDifference(nums=[3, 9, 7, 3]))
print(Solution().minimumDifference(nums=[-36, 36]))
print(Solution().minimumDifference(nums=[2, -1, 0, 4, -2, -9]))


'''
# cleaner O(2^(2*N)) solution which got TLE. The stupid leetcode is obviously looking for O(2^n) solution
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        possibleSums = set()
        self.dfsSearchToFindAllPossibleSums(nums, 0, possibleSums, 0, n, 0)

        ans = 2147483647
        numSum = sum(nums)
        for possibleSum in possibleSums:
            sumOfTheOtherHalf = numSum - possibleSum
            ans = min(ans, abs(possibleSum - sumOfTheOtherHalf))

        return ans

    def dfsSearchToFindAllPossibleSums(self, nums: List[int], i: int, possibleSums: set, currSum: int, n: int, currSize: int):
        if currSize == n:
            possibleSums.add(currSum)
            return
        if i == len(nums):
            return

        self.dfsSearchToFindAllPossibleSums(nums, i + 1, possibleSums, currSum, n, currSize)
        self.dfsSearchToFindAllPossibleSums(nums, i + 1, possibleSums, currSum + nums[i], n, currSize + 1)

'''
