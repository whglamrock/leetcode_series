
# Real one-pass solution; the for + underneath while loop combination isn't really "one-pass".
# See 3-way partitioning: https://discuss.leetcode.com/topic/26181/ac-python-in-place-one-pass-solution-o-n-time-o-1-space-no-swap-no-count

class Solution(object):
    def sortColors(self, nums):

        if not nums:
            return []

        i = j = 0   # the k will be the moving pointer
        # we keep [0, i], (i, j], (j, k] three separate parts that store the 0, 1, 2 respectively
        # [0, k] keeps growing as k moves forward and [0. k] is sorted(nums[:k + 1])

        for k in xrange(len(nums)):
            # at this point we can always make sure k >= j >= i
            val = nums[k]
            nums[k] = 2
            if val < 2:    # when val == 0, both i and j need to += 1, so we do j += 1 first
                nums[j] = 1
                j += 1
            if val == 0:    # when val == 1, only j needs to do += 1, so we do it in the above
                nums[i] = 0
                i += 1



nums = [0, 1, 2, 2, 1, 0, 2, 1, 1, 2]
Solution().sortColors(nums)
print nums



'''
from collections import Counter

# naive counting sort solution

class Solution(object):
    def sortColors(self, nums):

        numCount = Counter(nums)
        for i in xrange(len(nums)):
            if numCount[0] > 0:
                nums[i] = 0
                numCount[0] -= 1
            elif numCount[1] > 0:
                nums[i] = 1
                numCount[1] -= 1
            else:
                nums[i] = 2
                numCount[2] -= 1
'''