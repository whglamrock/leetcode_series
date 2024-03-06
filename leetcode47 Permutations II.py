from typing import List

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


print(Solution().permuteUnique([1, 1, 1, 3]))
