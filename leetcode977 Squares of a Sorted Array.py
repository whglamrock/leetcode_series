from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        indexOfMinNonNegative = self.findIndexOfMinNonNegative(nums)
        ans = []
        if indexOfMinNonNegative == -1:
            for i in range(len(nums) - 1, -1, -1):
                ans.append(nums[i] * nums[i])
        else:
            l, r = indexOfMinNonNegative - 1, indexOfMinNonNegative
            while l >= 0 and r < len(nums):
                if nums[l] * nums[l] <= nums[r] * nums[r]:
                    ans.append(nums[l] * nums[l])
                    l -= 1
                else:
                    ans.append(nums[r] * nums[r])
                    r += 1
            while l >= 0:
                ans.append(nums[l] * nums[l])
                l -= 1
            while r < len(nums):
                ans.append(nums[r] * nums[r])
                r += 1

        return ans

    def findIndexOfMinNonNegative(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if l == r:
                if nums[m] >= 0:
                    return m
                return -1
            if nums[m] < 0:
                l = m + 1
            else:
                r = m

        return -1


print(Solution().sortedSquares(nums=[-4, -1, 0, 3, 10]))
print(Solution().sortedSquares(nums=[-7, -3, 2, 3, 11]))
