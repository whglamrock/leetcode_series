
# unusual dp solution with memoization that records all possible previous sums

class Solution(object):
    def canPartition(self, nums):

        target = sum(nums)
        if target % 2 != 0: return False
        target /= 2

        sumset = set()
        sumset.add(0)
        for num in nums:
            if target - num in sumset:
                return True
            newsum = set()
            for sumvalue in sumset:
                newsum.add(sumvalue + num)
            sumset |= newsum

        return False



'''
# top-down naive backtracking solution
class Solution(object):
    def canFindSum(self, nums, target, ind, n, d):
        if target in d: return d[target]
        if target == 0: d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in xrange(ind, n):
                    if self.canFindSum(nums, target - nums[i], i+1, n, d):
                        d[target] = True
                        break
        return d[target]

    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0: return False
        return self.canFindSum(nums, s/2, 0, len(nums), {})
'''
