from typing import List

# decreasing stack + loop twice
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(n):
            while stack and stack[-1][1] < nums[i]:
                prevIndex, prevNum = stack.pop()
                ans[prevIndex] = nums[i]
            stack.append([i, nums[i]])
        for i in range(n):
            while stack and stack[-1][1] < nums[i]:
                prevIndex, prevNum = stack.pop()
                ans[prevIndex] = nums[i]
            stack.append([i, nums[i]])

        return ans
