# 'reach' is the farthest position to which nums[i] can jump
class Solution(object):
    def canJump(self, nums):

        reach = 0
        for i in xrange(len(nums)):
            if reach >= i and i+nums[i] > reach:
                reach = i+nums[i]

        return reach >= len(nums)-1

# It doesn't matter what value nums[-1] stores, cuz it won't e used.
# keep reading the question description until you can understand...it's confusing...