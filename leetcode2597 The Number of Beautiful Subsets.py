from collections import defaultdict
from typing import List, Dict

# remember this backtracking solution using the number counter approach (the trick of numCount[num] -= 1 after dfs).
class Solution:
    def __init__(self):
        # use a non local variable for dfs/backtracking
        self.ans = 0

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.ans = 0
        nums.sort()
        numCount = defaultdict(int)
        self.dfs(nums, k, 0, numCount)

        # exclude the empty set. in the dfs logic, if we keep not using nums[i],
        # it will result in one empty set scenario
        return self.ans - 1

    # dfs & backtracking
    def dfs(self, nums: List[int], k: int, i: int, numCount: Dict[int, int]):
        if i == len(nums):
            self.ans += 1
            return
        num = nums[i]
        if numCount[num - k] == 0:
            numCount[num] += 1
            # do dfs with this number used for the subset
            self.dfs(nums, k, i + 1, numCount)
            numCount[num] -= 1

        # do dfs without this number used for the subset
        self.dfs(nums, k, i + 1, numCount)


print(Solution().beautifulSubsets(nums=[2, 4, 6], k=2))
print(Solution().beautifulSubsets(nums=[1], k=1))
print(Solution().beautifulSubsets(nums=[10, 4, 5, 7, 2, 1], k=3))
