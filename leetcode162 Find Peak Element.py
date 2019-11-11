
# Idea: we keep nums[l - 1] < nums[l] and nums[r + 1] < num[r], so [l:r + 1] is always the candidate area

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            # whenever l < r, mPlusOne will be in range [0:len(nums)]
            mPlusOne = m + 1
            if nums[m] > nums[mPlusOne]:
                r = m
            # nums[m] != nums[mPlusOne] according to the problem definition
            else:
                l = mPlusOne

        return l



print Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
print Solution().findPeakElement([1, 2, 3, 1])
print Solution().findPeakElement([1, 2, 1, 3, 5, 6, 1])