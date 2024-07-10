from typing import List


# O(n) dp solution. for dp[i], if some tap on the right side of i (can include i) opens and the
# left most (> 0) watered point is i, dp[i] stores the corresponding right most watered point
# check: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/solutions/3983936/3-minutes-to-realise-greedy-approach-beats-99/
# P.S. The idea can originally come from the O(nlogn) sort ranges and find the most rightward overlapping
# range approach (code commented at the bottom).
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] * (n + 1)
        for i, radius in enumerate(ranges):
            if radius == 0:
                continue
            leftMostWateredPoint = max(0, i - radius)
            dp[leftMostWateredPoint] = max(dp[leftMostWateredPoint], i + radius)

        ans = 0
        currWateredSegment = 0
        rightMostWateredPoint = 0
        # make sure all segments before i is watered
        for i, rightBorder in enumerate(dp):
            # potentially have an un-watered segment, so need to open a tap
            if i > currWateredSegment:
                if rightMostWateredPoint < i:
                    return -1
                ans += 1
                currWateredSegment = rightMostWateredPoint

            rightMostWateredPoint = max(rightMostWateredPoint, rightBorder)

        return ans


print(Solution().minTaps(5, [3, 5, 1, 1, 0, 0]))
print(Solution().minTaps(3, [0, 0, 0, 0]))
print(Solution().minTaps(6, [1, 0, 2, 2, 0, 1, 0]))
print(Solution().minTaps(3, [1, 0, 0, 1]))
print(Solution().minTaps(6, [1, 0, 1, 2, 0, 1, 0]))
print(Solution().minTaps(5, [4, 1, 1, 1, 1, 1]))


'''
# O(N * log(N)) sorting solution, way easier to remember/implement
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        tapRanges = []
        for i, radius in enumerate(ranges):
            if radius == 0:
                continue
            leftBound = max(0, i - radius)
            rightBound = min(n, i + radius)
            tapRanges.append((leftBound, rightBound))
        tapRanges.sort()

        # dedupe
        distinctRanges = []
        for l, r in tapRanges:
            # same left bound
            if distinctRanges and l == distinctRanges[-1][0]:
                distinctRanges[-1][1] = r
                continue
            # combine ranges
            if distinctRanges and r <= distinctRanges[-1][1]:
                continue
            distinctRanges.append([l, r])
        
        # the below while loop checks for gap but it doesn't check for [0, first] and [last, n]
        if not distinctRanges or distinctRanges[0][0] != 0 or distinctRanges[-1][1] < n:
            return -1
        
        taps = []
        i = 0
        while i < len(distinctRanges):
            # no overlap
            if taps and taps[-1][1] < distinctRanges[i][0]:
                return -1

            # find the range with the farthest right bound that overlaps with taps[-1]
            while taps and i + 1 < len(distinctRanges) and distinctRanges[i + 1][0] <= taps[-1][1] and distinctRanges[i + 1][1] >= distinctRanges[i][1]:
                i += 1
            taps.append(distinctRanges[i])
            i += 1
        
        return len(taps)        
'''