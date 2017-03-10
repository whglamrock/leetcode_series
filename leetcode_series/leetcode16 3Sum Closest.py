
# Detailed idea and algorithm is referenced from leetcode15: 3Sum.

class Solution(object):
    def threeSumClosest(self, nums, target):

        if (not nums) or len(nums) < 3:
            return

        nums.sort()
        diff = abs(nums[0] + nums[1] + nums[2] - target)
        ans = nums[0] + nums[1] + nums[2]
        for i in xrange(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                newsum = nums[i] + nums[l] + nums[r]
                if abs(newsum - target) < diff:
                    diff = abs(newsum - target)
                    ans = newsum
                if newsum < target:
                    l += 1
                elif newsum > target:
                    r -= 1
                else:
                    return newsum
        return ans



nums = [-1,2,1,-4]
target = 1
Sol = Solution()
print Sol.threeSumClosest(nums,target)





