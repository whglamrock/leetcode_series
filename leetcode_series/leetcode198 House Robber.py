
# -*- coding: utf-8 -*-
'''
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
'''

class Solution:
    def rob(self, nums):
        last, now = 0, 0
        for i in nums:      # last相当于f(k-2),i相当于nums[k],now相当于f(k-1)
            last, now = now, max(last + i, now)      # f(0),f(1)也可以写成f(k)的形式,只是多几个0而已
        return now



a = [1,3,1]
Sol = Solution()
print Sol.rob(a)

