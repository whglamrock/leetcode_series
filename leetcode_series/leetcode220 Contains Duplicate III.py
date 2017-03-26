
# O(N) solution. idea is bucket sort.
# idea from: https://discuss.leetcode.com/topic/19991/o-n-python-using-buckets-with-explanation-10-lines

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):

        bucket = {}
        for i, num in enumerate(nums):
            if t != 0:
                bucketnum = num / t
                offset = 1
            else:
                bucketnum = num
                offset = 0

            for j in xrange(bucketnum - offset, bucketnum + offset + 1):
                if j in bucket and abs(bucket[j] - num) <= t:
                    return True

            bucket[bucketnum] = num
            # for nums[i], we always look for solution from previous k numbers(i-k ~ i).
            if len(bucket) > k:
                if t != 0:
                    del bucket[nums[i - k] / t]    # because the key corresponding to nums[i-k] is (i-k)'s bucket num,
                    # which is nums[i - k]/t
                else:
                    del bucket[nums[i - k]]

        return False