from typing import List

# the condition of such array exists is actually very strict:
# 1) The assuming it's nums[i:j], this means nums[:i] and nums[j + 1:] are non-decreasing
# 2) each element in nums[:i] and nums[j + 1:] is bigger than all of its left and smaller than all of its right
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        indexesBiggerThanLeft, indexesSmallerThanRight = [False] * n, [False] * n
        currMax = nums[0]
        for i, num in enumerate(nums):
            if num >= currMax:
                indexesBiggerThanLeft[i] = True
            currMax = max(currMax, num)
        currMin = nums[-1]
        for i in range(n - 1, -1, -1):
            if nums[i] <= currMin:
                indexesSmallerThanRight[i] = True
            currMin = min(currMin, nums[i])

        leftIndexCandidate = -1
        for i in range(n):
            if (i > 0 and nums[i] < nums[i - 1]) or not (indexesBiggerThanLeft[i] and indexesSmallerThanRight[i]):
                break
            leftIndexCandidate = i
        rightIndexCandidate = n
        for i in range(n - 1, -1, -1):
            if (i < n - 1 and nums[i] > nums[i + 1]) or not (indexesBiggerThanLeft[i] and indexesSmallerThanRight[i]):
                break
            rightIndexCandidate = i

        # the candidate subarray is nums[leftIndexCandidate + 1:rightIndexCandidate]
        if rightIndexCandidate - 1 >= leftIndexCandidate + 1:
            return rightIndexCandidate - leftIndexCandidate - 1
        else:
            return 0


print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(Solution().findUnsortedSubarray([1, 2, 3, 4]))
print(Solution().findUnsortedSubarray([1]))
print(Solution().findUnsortedSubarray([1, 2, 4, 3, 5, 6]))
print(Solution().findUnsortedSubarray([6, 4, 2, 8, 10, 9, 15]))
print(Solution().findUnsortedSubarray([5, 5, 5, 4, 4]))
