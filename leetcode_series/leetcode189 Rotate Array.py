'''
class Solution(object):
    def rotate(self, nums, k):

        numscopy = []
        for i in xrange(len(nums)):
            numscopy.append(nums[i])

        for i in xrange(len(nums)):
            nums[(i+k)%len(nums)] = numscopy[i]

        return nums


class Solution(object):
    def rotate(self, nums, k):

        for i in range(k):
            x = nums.pop()
            nums.insert(0,x)

        return nums

'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums)-k:]+nums[:len(nums)-k]
        return nums

a = [1,2,3,4,5,6]
k = 2
Sol = Solution()
print Sol.rotate(a,k)
