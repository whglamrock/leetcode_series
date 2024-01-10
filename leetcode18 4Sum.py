from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        self.findKSum(sorted(nums), target, 4, [], ans)
        return ans

    def findKSum(self, nums: List[int], target: int, k: int, curr: List[int], ans: List[List[int]]):
        # it's assumed k will >= 2
        if len(nums) < k or k < 2 or target < nums[0] * k or target > nums[-1] * k:
            return

        if k == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum == target:
                    ans.append(curr + [nums[l], nums[r]])
                    while l + 1 < len(nums) and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
                elif twoSum < target:
                    while l + 1 < len(nums) and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
                else:
                    while r - 1 >= 0 and nums[r - 1] == nums[r]:
                        r -= 1
                    r -= 1
        else:
            for i in range(len(nums) - k + 1):
                # avoid searching for the same numbers
                if i == 0 or nums[i - 1] != nums[i]:
                    self.findKSum(nums[i + 1:], target - nums[i], k - 1, curr + [nums[i]], ans)


print(Solution().fourSum([0, 1, 5, 0, 1, 5, 5, -4], 11))


'''
# simple dfs solution that got TLE
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = set()
        self.dfs(4, nums, '', 0, 0, target, quadruplets)
        ans = [] 
        for encodedIndexStr in quadruplets:
            indexesInStr = encodedIndexStr.split(',')
            indexes = [int(item) for item in indexesInStr]
            ans.append(indexes)
        return ans
    
    def dfs(self, k: int, nums: List[int], curr: str, currSum: int, i: int, target: int, quadruplets: set):
        if k == 0:
            if currSum == target:
                quadruplets.add(curr)
            return
        if i >= len(nums):
            return
        
        # choose i
        self.dfs(k - 1, nums, curr + ',' + str(nums[i]) if curr else str(nums[i]), currSum + nums[i], i + 1, target, quadruplets)
        # not choose i
        self.dfs(k, nums, curr, currSum, i + 1, target, quadruplets)
'''