
class NumArray(object):
    def __init__(self, nums):

        self.nums = [0]+nums
        for x in xrange(1,len(self.nums)):
            self.nums[x] += self.nums[x-1]

    def sumRange(self, i, j):
        
        if not self.nums:
            return 0
        return self.nums[j+1] - self.nums[i]



nums = [-2, 0, 3, -5, 2, -1]
Sol = NumArray(nums)
print Sol.sumRange(0,5)



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)