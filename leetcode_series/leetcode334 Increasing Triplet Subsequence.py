
# two pointers to record the current smallest and second smallest.
# read the fucking, code, no fucking reference.

class Solution(object):
    def increasingTriplet(self, nums):

        if not nums or len(nums) < 3:
            return False

        first = second = 2147483647
        for num in nums:
            if num <= first:    # remember it's "<=", not "<"
                first = num
            # it' elif, not if!
            elif num <= second:    # it's "<=", not "<"
                second = num
            else:
                return True
            
        return False



Sol = Solution()
nums = [9,4,3,1,6,2,8]
print Sol.increasingTriplet(nums)