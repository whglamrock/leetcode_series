
# key is use sumarray and hash table to search

class Solution(object):
    def maxSubArrayLen(self, nums, k):

        if not nums:
            return 0

        sumarray = []
        sumdic = {0: -1}
        ans = 0
        for i in xrange(len(nums)):
            newsum = sumarray[-1] + nums[i] if sumarray else nums[i]
            sumarray.append(newsum)
            # if the sum value is already already occurred we don't update because we only
            #   need the smallest index to product the longest subarray
            if newsum not in sumdic:
                sumdic[newsum] = i
            if newsum - k in sumdic:
                ans = max(ans, i - sumdic[newsum - k])

        return ans



Sol = Solution()
nums = [1, -1, 5, -2, 3]
k = 3
print Sol.maxSubArrayLen(nums, k)
