
# A dedicate solution using pigeonhole principle.
#   see explanation from: https://discuss.leetcode.com/topic/80841/python-with-explanation-62ms-time-o-min-n-k-mostly/2

class Solution(object):
    def checkSubarraySum(self, nums, k):

        if k == 0:
            for i in xrange(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        k = abs(k)
        # pigeonhole principle.
        if len(nums) >= 2 * k:
            return True

        sumarray = [0]
        for num in nums:
            # we only need the remainder here
            sumarray.append((sumarray[-1] + num) % k)

        dic = {}
        for i, sumvalue in enumerate(sumarray):
            if sumvalue in dic:
                if i - dic[sumvalue] >= 2:
                    return True
            else:
                dic[sumvalue] = i

        return False