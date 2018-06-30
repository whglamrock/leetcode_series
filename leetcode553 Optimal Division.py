
# idea: Mathematical induction(shu xue gui na fa), to prove X1/(X2/X3/X4/X5...) is the biggest
# also refer to: https://leetcode.com/problems/optimal-division/discuss/125607/Java-Solution-with-explanation

class Solution(object):
    def optimalDivision(self, nums):

        if not nums:
            return ''
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return '/'.join([str(nums[0]), str(nums[1])])
        strlist = [str(nums[0]), '/(', str(nums[1])]
        for num in nums[2:]:
            strlist.append('/')
            strlist.append(str(num))
        strlist.append(')')
        return ''.join(strlist)
