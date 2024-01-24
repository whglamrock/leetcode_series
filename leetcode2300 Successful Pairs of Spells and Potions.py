from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for spell in spells:
            target = success / spell
            ans.append(self.findNumOfElementsBiggerOrEqualThan(potions, target))

        return ans

    def findNumOfElementsBiggerOrEqualThan(self, nums: List[int], target: float) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                if nums[l] >= target:
                    return len(nums) - l
                else:
                    return 0
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        return 0


print(Solution().successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
print(Solution().successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
