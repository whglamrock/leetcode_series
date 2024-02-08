from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        ans = []
        for i in range(m):
            left, right = l[i], r[i]
            numSet = set(nums[left:right + 1])
            minNum, maxMum = min(numSet), max(numSet)
            if maxMum == minNum:
                ans.append(True)
                continue
            if (maxMum - minNum) % (right - left) != 0:
                ans.append(False)
                continue

            diff = (maxMum - minNum) // (right - left)
            canFormArithmetic = True
            for num in range(minNum, maxMum + 1, diff):
                if num not in numSet:
                    canFormArithmetic = False
                    break
            ans.append(canFormArithmetic)

        return ans
