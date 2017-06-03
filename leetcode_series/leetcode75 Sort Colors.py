
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

        #return nums    # leetcode asks to return nothing



nums = [0, 1, 2, 2, 1, 0, 2, 1, 1, 2]
Sol = Solution()
print Sol.sortColors(nums)



'''
# naive counting sort solution, based on that we already know what value we need:

class Solution(object):
    def sortColors(self, nums):

        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0: count0 += 1
            if num == 1: count1 += 1
            if num == 2: count2 += 1

        count1, count2 = count0 + count1, count0 + count1 + count2
        i = 0
        while i < count0:
            nums[i] = 0
            i += 1
        while i < count1:
            nums[i] = 1
            i += 1
        while i < count2:
            nums[i] = 2
            i += 1
'''