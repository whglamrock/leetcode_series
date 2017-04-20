
# real one-pass solution. The for + underneath while loop combination is not really "one-pass"

class Solution(object):
    def sortColors(self, nums):

        if not nums:
            return []

        i = j = 0
        for k in xrange(len(nums)):
            val = nums[k]
            nums[k] = 2
            if val < 2:
                nums[j] = 1
                j += 1
            if val == 0:
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