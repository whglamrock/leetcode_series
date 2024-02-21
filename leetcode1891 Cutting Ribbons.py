from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l, r = 1, sum(ribbons) // k
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if self.canCutKRibbonsOfLength(ribbons, k, m):
                    return m
                else:
                    return 0
            if self.canCutKRibbonsOfLength(ribbons, k, m):
                l = m
            else:
                r = m - 1

        return 0

    def canCutKRibbonsOfLength(self, ribbons: List[int], k: int, ribbonLen: int) -> bool:
        totalRibbons = 0
        for ribbon in ribbons:
            totalRibbons += ribbon // ribbonLen
            if totalRibbons >= k:
                return True

        return False
