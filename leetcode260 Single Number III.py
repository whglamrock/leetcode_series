from collections import Counter
from typing import List

# To solve it in O(n) space you will need bit manipulation. Fuck the bit manipulation!
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        numCount = Counter(nums)
        ans = []
        for num in numCount:
            if numCount[num] == 1:
                ans.append(num)
        return ans
