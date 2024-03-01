from collections import defaultdict
from typing import List

# doordash phone screen question: https://leetcode.com/discuss/interview-question/1379696/doordash-onsite
class Solution:
    def findNearestCity(self, cities: List[str], x: List[int], y: List[int], queries: List[str]) -> List[str]:
        xToYs = defaultdict(set)
        yToXs = defaultdict(set)
        coordinateToCity = {}
        cityToCoordinate = {}
        n = len(cities)
        for i in range(n):
            city, xValue, yValue = cities[i], x[i], y[i]
            coordinateToCity[(xValue, yValue)] = city
            cityToCoordinate[city] = [xValue, yValue]
            xToYs[xValue].add(yValue)
            yToXs[yValue].add(xValue)

        for xValue in xToYs:
            xToYs[xValue] = sorted(xToYs[xValue])
        for yValue in yToXs:
            yToXs[yValue] = sorted(yToXs[yValue])

        ans = []
        for i, city in enumerate(queries):
            xValue, yValue = cityToCoordinate[city]
            if xValue not in xToYs or yValue not in yToXs:
                ans.append('NONE')
                continue
            if len(xToYs[xValue]) == 1 and len(yToXs[yValue]) == 1:
                ans.append('NONE')
                continue

            candidates = []
            xValuesWithSameY = yToXs[yValue]
            closestSmallerX = self.findClosestSmallerValue(xValuesWithSameY, xValue)
            closestBiggerX = self.findClosestBiggerValue(xValuesWithSameY, xValue)
            closestXCity = None
            if closestSmallerX != -1 and closestBiggerX != -1:
                closestCities = [coordinateToCity[(closestSmallerX, yValue)], coordinateToCity[(closestBiggerX, yValue)]]
                closestXCity = sorted(closestCities)[0]
            elif closestSmallerX == -1 and closestBiggerX != -1:
                closestXCity = coordinateToCity[(closestBiggerX, yValue)]
            elif closestSmallerX != -1 and closestBiggerX == -1:
                closestXCity = coordinateToCity[(closestSmallerX, yValue)]
            if closestXCity is not None:
                candidates.append(closestXCity)

            yValuesWithSameX = xToYs[xValue]
            closestSmallerY = self.findClosestSmallerValue(yValuesWithSameX, yValue)
            closestBiggerY = self.findClosestBiggerValue(yValuesWithSameX, yValue)
            closestYCity = None
            if closestSmallerY != -1 and closestBiggerY != -1:
                closestCities = [coordinateToCity[(xValue, closestSmallerY)], coordinateToCity[(xValue, closestBiggerY)]]
                closestYCity = sorted(closestCities)[0]
            elif closestSmallerY == -1 and closestBiggerY != -1:
                closestYCity = coordinateToCity[(xValue, closestBiggerY)]
            elif closestSmallerY != -1 and closestBiggerY == -1:
                closestYCity = coordinateToCity[(xValue, closestSmallerY)]
            if closestYCity is not None:
                candidates.append(closestYCity)

            ans.append(sorted(candidates)[0])

        return ans

    # find the closest value > target
    def findClosestBiggerValue(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] <= target:
                    return -1
                return nums[m]
            if nums[m] <= target:
                l = m + 1
            else:
                r = m

    # find the closest value < target
    def findClosestSmallerValue(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if nums[m] >= target:
                    return -1
                return nums[m]
            if nums[m] >= target:
                r = m - 1
            else:
                l = m


print(Solution().findNearestCity(['biggestCity', 'bananaCity', 'xyz'], [20, 20, 20], [20, 10, 0], ['biggestCity', 'bananaCity', 'xyz']))
