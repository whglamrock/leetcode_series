from collections import Counter
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numCount = Counter(nums)
        ans = []
        while numCount:
            # try to put as many distinct numbers in each row as possible
            row = []
            numsToDelete = []
            for num in numCount:
                row.append(num)
                numCount[num] -= 1
                if not numCount[num]:
                    numsToDelete.append(num)
            for num in numsToDelete:
                del numCount[num]
            ans.append(row)

        return ans


print(Solution().findMatrix([1, 3, 4, 1, 2, 3, 1]))
