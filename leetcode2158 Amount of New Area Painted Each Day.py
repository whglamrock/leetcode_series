from typing import List

# jump the number line solution. see: https://leetcode.com/problems/amount-of-new-area-painted-each-day/solutions/1751389/jump-line/
# O(n + m) solution where m is the total length of all the paint areas
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        line = [0] * 500001
        ans = [0] * len(paint)

        for i, (start, end) in enumerate(paint):
            lengthPainted = 0
            while start < end:
                jump = max(line[start], start + 1)
                # if this slot is not painted
                if line[start] == 0:
                    lengthPainted += 1
                # compression: when line[start] is not 0 it was painted before
                # so we need to find the max jump
                line[start] = max(line[start], end)
                # if this (start, end) completely overlaps, it will exit the loop
                start = jump
            ans[i] = lengthPainted

        return ans


print(Solution().amountPainted(paint=[[1, 4], [4, 7], [5, 8]]))
print(Solution().amountPainted(paint=[[1, 4], [5, 8], [4, 7]]))
print(Solution().amountPainted(paint=[[1, 5], [2, 4]]))
