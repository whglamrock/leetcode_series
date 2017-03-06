# see my explanation from: https://discuss.leetcode.com/topic/42901/simple-9-line-python-solution
# or Stefan's: https://discuss.leetcode.com/topic/35494/solution-explanation
class Solution(object):
    def minPatches(self, nums, n):

        miss, i, added = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1

        return added