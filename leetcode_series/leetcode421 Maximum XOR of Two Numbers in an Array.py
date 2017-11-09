
# idea from: https://discuss.leetcode.com/topic/63213/java-o-n-solution-using-bit-manipulation-and-hashmap/7
# read the discussion in the above link, the idea is the build maixmum bit by bit from left to right

class Solution(object):
    def findMaximumXOR(self, nums):

        maximum, mask = 0, 0
        for i in xrange(31, -1, -1):
            mask += (1 << i)
            prefixes = set()
            #print mask
            for num in nums:
                prefixes.add(mask & num)
            #print prefixes

            tmp = maximum | (1 << i)    # tmp is candidate, represents a 'possibility'!
            #print tmp, maximum
            for prefix in prefixes:
                if tmp ^ prefix in prefixes:  # very important feature: if a ^ b = c, then b ^ c = a, c ^ a = b
                # the above if statement equals to: does there exist two prefixes a, b that a ^ b = tmp
                    maximum = tmp

        return maximum