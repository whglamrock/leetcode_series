
# real one-pass solution. The for + underneath while loop combination is not really "one-pass"
# three way partitioning, see explanation: https://discuss.leetcode.com/topic/26181/ac-python-in-place-one-pass-solution-o-n-time-o-1-space-no-swap-no-count

class Solution(object):
    def sortColors(self, nums):

        if not nums:
            return []

        i = j = 0   # the k will be the moving pointer
        # we keep [0, i), [i, j), [j, k) three separate parts that store the 0, 1, 2 respectively

        for k in xrange(len(nums)):
            val = nums[k]
            nums[k] = 2
            # the i and j before the "+= 1" are the end indices of 0s and 1s,
            #   so we know where to put the new val when nums[k] != 2
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