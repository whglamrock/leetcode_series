
# two pointers to record the current smallest and second smallest.
# read the fucking, code, no fucking reference.

class Solution(object):
    def increasingTriplet(self, nums):

        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False



Sol = Solution()
nums = [9,4,3,1,6,2,8]
print Sol.increasingTriplet(nums)