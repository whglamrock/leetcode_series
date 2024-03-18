from typing import List

# The idea is to try to insert number into gaps between elements in the current permutation and break the loop if the
# new number == any currPermutation[i].
# Use [1, 1, 2, 1] as example to see how you generate the permutations of length 4 from permutations of length 3,
# so we know why we break the inner for loop (lint 14) if we found a same number to avoid any duplicates.
class Solution(object):
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        curr = [[]]
        for num in nums:
            next = []
            for currPermutation in curr:
                for i in range(len(currPermutation) + 1):
                    next.append(currPermutation[:i] + [num] + currPermutation[i:])
                    # avoid duplicates
                    if i < len(currPermutation) and currPermutation[i] == num:
                        break
            curr = next

        return curr


print(Solution().permuteUnique([1, 1, 1, 2]))
