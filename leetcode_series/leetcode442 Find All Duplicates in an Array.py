
# use the nums itself as hashtable.

class Solution(object):
    def findDuplicates(self, nums):

        res = []
        for num in nums:
            i = abs(num) - 1
            if nums[i] < 0:
                res.append(abs(num))
            else:
                nums[i] *= -1

        return res