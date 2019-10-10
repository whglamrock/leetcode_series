
# the hard part is using constant space

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        nums.append(0)
        n = len(nums)

        # delete those useless numbers since they are not candidates
        for i in xrange(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0

        # use index as the hash key to count each number's frequency
        for i in xrange(n):
            # nums[i] may have been "+n"'ed a lot of times, so "%n" is to get the original value
            nums[nums[i] % n] += n

        for i in xrange(1, n):
            if nums[i] < n:
                return i

        return n



print Solution().firstMissingPositive([-2, 3, 7, 8, 9, 11, 12])