# in the following solution, 'compatible' means: after adding the new curNum to the previous subsets,
# they are still inter-divisible. If can't read the reference, rewrite every i & j for loop for our
# test case to understand.

from copy import copy
# P.S.: How could the copied list remain when the original list changes? Use the 'copy' operator!
class Solution(object):
    def largestDivisibleSubset(self, nums):

        nums.sort()
        n = len(nums)
        if n == 0: return []
        dp = [0] * n
        dp[0] = [nums[0]]

        for i in xrange(1, n):  # after the ith loop, dp[:i+1] are valid (i.e., = final dp[:i+1])
            curNum = nums[i]
            maxSet = []
            for j in xrange(i):  # every dp[j] is valid because dp[:i] are valid
                if curNum % nums[j] == 0:   # curNum is divisible by nums[j], then it must be divisible by
                    # every number in dp[j] that is less than nums[j]
                    localSet = copy(dp[j])
                    if len(localSet) > len(maxSet):
                        maxSet = localSet
            # The j for loop looks for longest subset with dp[:i] that's compatible with nums[i].
            # For two biggest dp[x], dp[y] within dp[:i] that are both compatible with nums[i],
            # the maxSet for nums[i] can only be either dp[x]+[nums[i]] or dp[y]+[nums[i]]!
            # Reasoning:
            # 1) Let's assume len(dp[y]) > len(dp[x]).
            # 2) If dp[x], dp[y] are incompatible and have common elements, all uncommon
            #   elements in dp[x] are causing the incompatibility. So if the maxSet for nums[i]
            #   = dp[y]+[nums[i]], all uncommon elements in dp[x] can not be added to this maxSet.
            # 3) If dp[x], dp[y] are incompatible and don't have common elements, the situation is even
            #   easier to think through
            # 4) If dp[x], dp[y] are compatible, then y must > x and all elements of dp[x] are included
            #   in dp[y]. Thus the maxSet for nums[i] -- dp[i] = dp[y]+[nums[i]]
            # All above proves that once we found the longest compatible subset dp[y] within dp[:i],
            # the dp[i] = dp[y]+[nums[i]] and there is no need to check other common elements in various
            # dp[j]s.

            maxSet.append(nums[i])  # after finding the previously longest subset, adding nums[i] itself.
            dp[i] = maxSet  # update the dp[i] for it to be used in next i for loop.

        res = []
        for localSet in dp:    # in final dp, dp[i] is the largest subset ends with nums[i]
            if len(localSet) > len(res):
                res = localSet
        return res


Sol = Solution()
nums = [1,2,3,4,6,24]
print Sol.largestDivisibleSubset(nums)