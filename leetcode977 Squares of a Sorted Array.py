from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        firstIndexLessThan0 = self.findFirstIndexLessThan0(nums)
        negatives = []
        if firstIndexLessThan0 != -1:
            negatives = nums[:firstIndexLessThan0 + 1]
            negatives.reverse()
        return self.mergeArrays(negatives, nums[firstIndexLessThan0 + 1:])

    # it's assumed that negatives are sorted in reverse order
    def mergeArrays(self, negatives: List[int], positives: List[int]) -> List[int]:
        merged = []
        i, j = 0, 0
        while i < len(negatives) and j < len(positives):
            if -negatives[i] < positives[j]:
                merged.append(negatives[i] * negatives[i])
                i += 1
            else:
                merged.append(positives[j] * positives[j])
                j += 1

        while i < len(negatives):
            merged.append(negatives[i] * negatives[i])
            i += 1

        while j < len(positives):
            merged.append(positives[j] * positives[j])
            j += 1

        return merged

    def findFirstIndexLessThan0(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r and nums[m] < 0:
                return m
            if nums[m] >= 0:
                r = m - 1
            else:
                l = m

        return -1


print(Solution().sortedSquares(nums=[-4, -1, 0, 3, 10]))
print(Solution().sortedSquares(nums=[-7, -3, 2, 3, 11]))
