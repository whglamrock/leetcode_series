from collections import deque
from typing import List

# idea from: https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/solutions/2640791/python3-make-first-and-last-number-same-then-delete-them/
# but it doesn't prove why the greedy approach yields the optimal answer.
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = deque(nums)
        prefix, suffix = 0, 0
        numOfOperations = 0
        while nums:
            # means prefix == suffix
            if prefix == 0:
                # to avoid popping empty nums
                if len(nums) == 1:
                    break
                prefix = nums.popleft()
                suffix = nums.pop()
            elif prefix == suffix:
                prefix, suffix = 0, 0
            elif prefix < suffix:
                prefix += nums.popleft()
                numOfOperations += 1
            else:
                suffix += nums.pop()
                numOfOperations += 1

        # in this case all nums are deleted and we just need to merge prefix and suffix into one number
        if prefix != suffix:
            return numOfOperations + 1
        return numOfOperations
