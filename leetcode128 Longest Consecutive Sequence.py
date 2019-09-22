class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        numSet = set(nums)
        maxLen = 0

        for num in nums:
            if num not in numSet:
                continue

            l, r = num - 1, num + 1
            while l in numSet:
                numSet.discard(l)
                l -= 1
            while r in numSet:
                numSet.discard(r)
                r += 1

            maxLen = max(maxLen, r - l - 1)

        return maxLen



print Solution().longestConsecutive([100, 1, 3, 4, 2, 6, 5, 8])




