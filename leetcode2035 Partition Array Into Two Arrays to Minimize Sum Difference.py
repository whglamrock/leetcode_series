from collections import defaultdict
from itertools import combinations
from typing import List, Dict

# Overall O(N * 2 ^ N) time complexity where len(nums) == 2 * N
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        leftHalf, rightHalf = nums[:n], nums[n:]
        leftPossibleSums, rightPossibleSums = self.generateAllPossibleSums(leftHalf), self.generateAllPossibleSums(rightHalf)

        minDiff = abs(sum(leftHalf) - sum(rightHalf))
        totalSum = sum(nums)
        halfSum = totalSum / 2
        # try to build array 1
        for i in range(1, n):
            leftSumsOfArray1 = leftPossibleSums[i]
            rightSumsOfArray1 = sorted(rightPossibleSums[n - i])
            for leftSum in leftSumsOfArray1:
                rightSum = self.findClosestNum(rightSumsOfArray1, halfSum - leftSum)
                sumOfArray1 = leftSum + rightSum
                minDiff = min(minDiff, abs(2 * sumOfArray1 - totalSum))

        return minDiff

    def generateAllPossibleSums(self, nums: List[int]) -> Dict[int, set]:
        possibleSums = defaultdict(set)
        for i in range(1, len(nums) + 1):
            for subset in combinations(nums, i):
                possibleSums[i].add(sum(subset))
        return possibleSums

    # find the smallest nums[i] >= target
    def findClosestNum(self, nums: List[int], target: float) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                return nums[m]
            if nums[m] == target:
                return nums[m]
            elif nums[m] < target:
                l = m + 1
            else:
                r = m

        # exit condition is l == r
        if l - 1 >= 0 and abs(nums[l - 1] - target) < abs(nums[l] - target):
            return nums[l - 1]
        return nums[l]


print(Solution().minimumDifference(nums=[3, 9, 7, 3]))
print(Solution().minimumDifference(nums=[-36, 36]))
print(Solution().minimumDifference(nums=[2, -1, 0, 4, -2, -9]))


'''
# cleaner O(2 ^ (2 * N)) solution which got TLE. The stupid leetcode is obviously looking for O(2 ^ n) solution
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