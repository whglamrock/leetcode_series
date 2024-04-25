from typing import List

# remember this solution. Remember to use dfs. It's easier to use dfs to dedupe instead of backtracking
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.dfs(ans, [], nums)
        return ans

    def dfs(self, ans: List[List[int]], path: List[int], nums: List[int]):
        ans.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # remember here we directly cut the nums array to dedupe instead of recording the index used in this dfs
            self.dfs(ans, path + [nums[i]], nums[i + 1:])
