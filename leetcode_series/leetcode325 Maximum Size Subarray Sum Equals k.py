
# key is use hash table to search

class Solution(object):
    def maxSubArrayLen(self, nums, k):

        if not nums:
            return 0

        sumvalue = 0
        # edge case when the desired subarray starts from the first element
        dic = {0: -1}
        res = 0

        for i in xrange(len(nums)):
            sumvalue += nums[i]
            # the dic always store the smallest end index of accumulate sumarray that sum to a specific value
            if sumvalue not in dic:
                dic[sumvalue] = i
            # i - dic[sumvalue - k], not dic[sumvalue] - dic[sumvalue - k]
            if sumvalue - k in dic:
                res = max(res, i - dic[sumvalue - k])

        return res

