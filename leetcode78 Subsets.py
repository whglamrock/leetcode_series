from copy import deepcopy
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = [[]]
        for num in nums:
            next = deepcopy(curr)
            for item in curr:
                next.append(item + [num])
            curr = next

        return curr


print(Solution().subsets([2, 1, 4, 3, 5]))
