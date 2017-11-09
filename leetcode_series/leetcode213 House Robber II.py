
# idea came from lc 198: House Robber

class Solution(object):
    def rob(self, nums):

        if (not nums):
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(list):
            last, now, flag = 0, 0, True
            for i in xrange(len(list)):
                if i == len(list)-1 and last+list[i] > now:
                    flag = False    # when the last one is chosen
                last, now = now, max(last+list[i], now)
            return [now, flag]

        re1 = helper(nums[2:])
        big1 = nums[0]+re1[0]   # choose the first one for sure
        flag1 = re1[1]

        re2 = helper(nums[3:])
        big2 = nums[1]+re2[0]   # choose the second one for sure (no limit for choosing the last one in this case)
        withoutlast = helper(nums[2:len(nums)-1])[0]+nums[0]   # when don't choose the last one but choose the first
        # notice that withoutlast isn't necessarily equal to big-nums[-1].

        if flag1 == False:  # the last one and the first one are chosen, so conflict must be resolved by:
            big1 = max(big1-nums[0], withoutlast)
        return max(big1, big2)