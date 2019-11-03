
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        numsSet = set(nums)
        longest = 1

        for num in nums:
            if num not in numsSet:
                continue
            numsSet.discard(num)

            l, r = num - 1, num + 1
            while l in numsSet:
                numsSet.discard(l)
                l -= 1
            while r in numsSet:
                numsSet.discard(r)
                r += 1

            longest = max(longest, r - l - 1)

        return longest



print Solution().longestConsecutive([100, 1, 3, 4, 2, 6, 5, 8])




