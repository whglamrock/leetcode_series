
'''
The permutation is literally "swap and sort": see line 24 and 25
'''

class Solution(object):
    def nextPermutation(self, nums):

        # Use two-pointers: two pointers start from back
        # first pointer j stop at descending point
        # second pointer i stop at value > nums[j]
        # swap and sort rest
        if not nums: return None
        i = len(nums)-1
        j = -1 # j is set to -1 for case `4321`, so need to reverse all in following step

        while i > 0:
            if nums[i] > nums[i-1]: # first one violates the trend
              j = i-1
              break
            i-=1

        for x in xrange(len(nums)-1, -1, -1):
            if nums[x] > nums[j]:
                nums[x], nums[j] = nums[j], nums[x] # swap position
                nums[j+1:] = sorted(nums[j+1:]) # sort rest
                return nums



Sol = Solution()
a = [1,3,4,2]
print Sol.nextPermutation(a)
