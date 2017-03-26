
# So called one-pass solution. Or we can cound the number of each of the three colors
# idea from: https://discuss.leetcode.com/topic/5422/share-my-one-pass-constant-space-10-line-solution

class Solution(object):
    def sortColors(self, nums):

        n = len(nums)
        two, zero = n - 1, 0
        for i in xrange(n):
            while nums[i] == 2 and i < two:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            while nums[i] == 0 and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

        #return nums