
# zeroright = the count of consecutive 1s on the left of this zero(or virtual zero) + 1.
#   where in the virtual zero case, there is no zero in the nums

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        ans, zeroright, zeroleft = 0, 0, 0

        for i, num in enumerate(nums):
            zeroright += 1
            if num == 0:
                zeroright, zeroleft = 0, zeroright
            # there is no need to do: ans = max(ans, zeroright + zeroleft + 1) because the
            #   the zeroright already contains the 1.
            ans = max(ans, zeroright + zeroleft)

        return ans