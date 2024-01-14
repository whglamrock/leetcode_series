from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, nums: List[int], curr: List[int], ans: List[List[int]]):
        if not nums:
            ans.append(curr)
            return

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], curr + [nums[i]], ans)


print(Solution().permute([1, 2, 3]))


'''
from math import factorial
from copy import deepcopy
from typing import List

# next permutation approach, but it's not optional due to suffix sorting
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [deepcopy(nums)]
        curr = nums
        while len(ans) < factorial(n):
            nextPermutation = self.findNextPermutation(curr)
            ans.append(deepcopy(nextPermutation))
            curr = nextPermutation

        return ans

    def findNextPermutation(self, nums: List[int]) -> List[int]:
        j = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                j = i - 1
                break
        # the nums are strictly decreasing
        if j == -1:
            return nums[::-1]
        for k in range(len(nums) - 1, j, -1):
            if nums[k] > nums[j]:
                break
        nums[k], nums[j] = nums[j], nums[k]
        return nums[:j + 1] + sorted(nums[j + 1:])
'''
