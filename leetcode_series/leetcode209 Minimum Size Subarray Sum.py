
# O(n) time, O(1) space solution
# keep a slicing window, the summary is the sum of subarray ends with nums[j], the
# window will always be the smallest window ends with nums[j].

class Solution(object):
    def minSubArrayLen(self, s, nums):

        if (not nums):
            return 0

        windowsum = 0
        leftindex = 0
        minlength = 2147483647

        for i in xrange(len(nums)):
            windowsum += nums[i]
            if windowsum >= s:
                while windowsum - nums[leftindex] >= s:
                    windowsum -= nums[leftindex]
                    leftindex += 1
                minlength = min(minlength, i - leftindex + 1)

        if minlength > len(nums): return 0
        return minlength



s = 7
nums = [2,3,1,2,4,3]
Sol = Solution()
print Sol.minSubArrayLen(s, nums)



'''
# the leetcode also asks for a 0(nlogn) solution...
# 0(nlogn) time, O(n) space solution
# idea from: https://discuss.leetcode.com/topic/13749/two-ac-solutions-in-java-with-time-complexity-of-n-and-nlogn-with-explanation/2
class Solution(object):
    def minSubArrayLen(self, s, nums):

        if (not nums) or len(nums) == 0:
            return 0

        def findright(l, r, array, target):
            start = l
            while l <= r:
                mid = l + (r - l) / 2
                if array[mid] - array[start] > target:
                    r = mid - 1
                elif array[mid] - array[start] == target:
                    return mid
                else:
                    l = mid + 1
            return min(l, len(array)-1)    # consider when array[-1] - array[start] < s,
            # l will = len(array). so we need to return a valid index.

        sumarray = [0] * (len(nums) + 1)    # cumulative value of nums. notice the length
        for i in xrange(1, len(nums) + 1):    # starts from 1, means sumarray[0] = 0
            sumarray[i] = sumarray[i-1] + nums[i-1]

        res = 2147483647
        for i in xrange(len(nums) + 1):
            j = findright(i, len(nums), sumarray, s)
            if sumarray[j] - sumarray[i] >= s and j - i < res:
                res = j - i    # considering the findright function will always return a index
                # even if "array[-1] - array[start] < s", we need to make sure j - i is
                # meaningful, by adding "sumarray[j] - sumarray[i] >= s".

        if res == 2147483647:
            return 0
        return res
'''
