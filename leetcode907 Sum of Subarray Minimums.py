from typing import List

# remember to use chunkSum to more easily deal with edge case
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        windowSum = 0
        mod = 10 ** 9 + 7

        for i, num in enumerate(arr):
            while stack and stack[-1][1] > num:
                prevIndex, prevMin, prevChunkSum = stack.pop()
                windowSum -= prevChunkSum

            # current num is the smallest so far
            if not stack:
                chunkSum = num * (i + 1)
            else:
                chunkSum = num * (i - stack[-1][0])
            windowSum += chunkSum
            stack.append([i, num, chunkSum])
            ans += windowSum

        return ans % mod


print(Solution().sumSubarrayMins([3, 1, 2, 4, 1]))
print(Solution().sumSubarrayMins([85, 93, 93, 90]))
# 1) Edge case like below makes chunkSum useful. Otherwise you will have to deal edge case where sometimes
# (i - stack[-1][0]) need to be replaced with (i - stack[-1][0] - 1).
# 2) e.g., when i is at 32 (i = 9), the stack is [[4, 18, chunkSum], [6, 41, chunkSum], [8, 51, chunkSum]]
# 3) without chunkSum we will need to do following operation for windowSum:
# pop out [8, 51, chunkSum], windowSum -= (9 - 6 - 1) * 51
# pop out [6, 41, chunkSum], windowSum -= (6 - 4) * 41 --> notice here we don't have to do extra "-1"
print(Solution().sumSubarrayMins([35, 26, 60, 45, 18, 48, 41, 57, 51, 32]))
