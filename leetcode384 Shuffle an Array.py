from random import randint
from copy import deepcopy
from typing import List

# idea from: https://discuss.leetcode.com/topic/53985/well-explained-o-n-java-solution-by-using-random-class-and-swapping-current-with-a-random-previous-index
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        ans = deepcopy(self.nums)
        for i in range(1, len(ans)):
            # randint is inclusive for both ends
            j = randint(0, i)
            ans[i], ans[j] = ans[j], ans[i]
        return ans
