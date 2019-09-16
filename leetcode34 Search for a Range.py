
# Idea: find the target value first, then search the start/last in the left/right half

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        position = self.findTarget(nums, target)
        if position == -1:
            return [-1, -1]

        # print position
        first, last = position, position

        # find the first appearance
        l, r = 0, position
        while l <= r:
            if l == r and nums[l] == target:
                first = l
                break
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            # else then nums[m] must == target
            else:
                r = m

        # find the last appearance
        l, r = position, len(nums) - 1
        while l <= r:
            if l == r and nums[l] == target:
                last = l
                break
            # we wanna make sure that when r = l + 1, the m = r to avoid infinite while loop; also this way we can still always keep [l, r] valid range inclusive
            m = (l + r + 1) / 2
            if nums[m] > target:
                r = m - 1
            # else then nums[m] must == target
            else:
                l = m

        return [first, last]

    def findTarget(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1



print Solution().searchRange([2, 2], 2)