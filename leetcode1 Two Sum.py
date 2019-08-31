
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
