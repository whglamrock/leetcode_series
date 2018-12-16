
class Solution(object):
    def firstMissingPositive(self, nums):
        if not nums:
            return 1

        k = self.partition(nums) + 1
        # to deal with case like [1, 2, 0] when the first missing positive integer is bigger than all positive interfers
        firstMissingIndex = k

        for i in xrange(k):
            tmp = abs(nums[i])
            if tmp <= k:  # use <= because we need tmp - 1
                # make nums[tmp - 1] negative to indicate tmp exists
                nums[tmp - 1] = -abs(nums[tmp - 1])  # not directly -nums[tmp - 1] because numbs can contain duplicates

        for i in xrange(k):
            if nums[i] > 0:  # indicates integer i + 1 doesn't exist
                firstMissingIndex = i
                break

        return firstMissingIndex + 1

    # put negative integers to the right of the nums array
    def partition(self, nums):
        n = len(nums)
        q = -1
        # q actually records the index of un-swapped negative integers
        for i in xrange(n):
            if nums[i] > 0:
                q += 1
                self.swap(nums, q, i)
        return q

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
