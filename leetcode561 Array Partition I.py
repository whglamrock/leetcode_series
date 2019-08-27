
# for algorithm explanation: https://leetcode.com/problems/array-partition-i/discuss/102208/JavaC%2B%2B-Clean-Code-1-sentence-explanation

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([nums[i] for i in xrange(0, len(nums), 2)])