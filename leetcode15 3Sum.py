
# The stupid leetcode OJ TLE the python non-sort O(n^2) solution(while exactly same java solution gets AC).
    # in real interview the python solution will work

class Solution(object):
    def threeSum(self, nums):

        if not nums or len(nums) < 3:
            return []

        n = len(nums)
        nums.sort()
        ans = []

        for i in xrange(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # check the duplicates here instead of at the beginning of the big while loop
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # put the following here then they won't affect the above while loops
                    l += 1
                    r -= 1

        return ans



print Solution().threeSum([0, 0, 0])



'''
# the following will definitely word in a real interview. Stupid motherfucking leetcode

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        
        numToIndex = {}
        for i, num in enumerate(nums):
            # for duplicate numbers we only need the last index
            numToIndex[num] = i
        
        ans = set()
        n = len(nums)
        for i in xrange(n - 2):
            target = 0 - nums[i]
            for j in xrange(i + 1, n - 1):
                if target - nums[j] in numToIndex and numToIndex[target - nums[j]] > j:
                    triplet = sorted([nums[i], nums[j], target - nums[j]])
                    ans.add((triplet[0], triplet[1], triplet[2]))
        
        ans = [list(item) for item in ans]
        return ans
'''










