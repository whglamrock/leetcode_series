from typing import List

# P.S. How negative numbers are saved in binary: https://courses.cs.washington.edu/courses/cse390b/21sp/readings/negative_binary.html
# How binary is constructed/queried: https://www.hackerearth.com/practice/notes/binary-indexed-tree-or-fenwick-tree/
class Solution(object):
    def countSmaller(self, nums: List[int]) -> List[int]:
        # BIT is non-0 index based array because we need to perform bit operation on index
        ranks = {num: rank + 1 for rank, num in enumerate(sorted(set(nums)))}
        bit = [0] * (len(ranks) + 1)

        ans = []
        for num in nums[::-1]:
            count = self.queryBIT(bit, ranks[num] - 1)
            ans.append(count)
            self.updateBIT(bit, ranks[num])

        return ans[::-1]

    def updateBIT(self, bit, i):
        while i < len(bit):
            bit[i] += 1
            i += (i & -i)

    def queryBIT(self, bit, i):
        ans = 0
        while i > 0:
            ans += bit[i]
            i -= (i & -i)
        return ans


print(Solution().countSmaller([5, 6, 2, 1, 3, 4, 7, 8, 10]))
