from typing import List

# P.S. How negative numbers are saved in binary: https://courses.cs.washington.edu/courses/cse390b/21sp/readings/negative_binary.html
# How binary is constructed/queried: https://www.hackerearth.com/practice/notes/binary-indexed-tree-or-fenwick-tree/
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # BIT is non-0 index based array because we need to perform bit operation on index
        numToRank = {}
        for i, num in enumerate(sorted(set(nums))):
            numToRank[num] = i + 1
        bit = [0] * (len(numToRank) + 1)

        ans = []
        for num in nums[::-1]:
            # O(log(N)) time because len(numToRank) <= N
            countOfLowerRankNumbers = self.query(bit, numToRank[num] - 1)
            ans.append(countOfLowerRankNumbers)
            # add the count of this rank by + 1. O(log(N)) time because len(numToRank) <= N
            self.update(bit, numToRank[num])

        return ans[::-1]

    def update(self, bit: List[int], i: int):
        while i < len(bit):
            bit[i] += 1
            i += (i & -i)

    def query(self, bit: List[int], i: int) -> int:
        prefixSum = 0
        while i > 0:
            prefixSum += bit[i]
            i -= (i & -i)
        return prefixSum


print(Solution().countSmaller([5, 6, 2, 1, 3, 4, 7, 8, 10]))
