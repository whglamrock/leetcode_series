
# use mask to count the number of elements that have 1 at position i, so the position i will
# contribute count * (n - count) to the total hamming distance.

# see detail: https://discuss.leetcode.com/topic/72092/java-o-n-time-o-1-space

class Solution(object):
    def totalHammingDistance(self, nums):

        total = 0
        n = len(nums)
        mask = 1

        for i in xrange(32):
            count = 0
            for j in xrange(n):
                if nums[j] & mask == mask:
                    count += 1
            total += count * (n - count)
            mask <<= 1

        return total