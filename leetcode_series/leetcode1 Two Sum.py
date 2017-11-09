
# O(N) hash-table solution

class Solution(object):

    def twoSum(self, nums, target):

        if nums is None or not nums:
            return []

        valueToIndex = {}
        for i, num in enumerate(nums):
            if target - num in valueToIndex:
                return [valueToIndex[target - num], i]
            valueToIndex[num] = i

        return []



'''
# in lintcode, several edge cases need to be considered.

class Solution:

    def twoSum(self, nums, target):
        # write your code here
        if (not nums): return []

        dick = {}
        for i in xrange(len(nums)):
            if nums[i] not in dick:
                dick[nums[i]] = [i]
            else:
                dick[nums[i]].append(i)

        ans = []
        for num in dick:
            if target - num in dick:
                if target - num == num:
                    if num == 0 and len(dick[num]) == 1:   # this doesn't but double 0s work
                        continue
                    elif len(dick[num]) > 1:  # if len(dick[num]) == 1, we can't choose num
                        ans.append(dick[num][0])
                        ans.append(dick[num][1])
                elif target - num != num:    # normal case
                    ans.append(dick[num][0])
                    ans.append(dick[target-num][0])
                break

        ans.sort()
        return ans
'''
