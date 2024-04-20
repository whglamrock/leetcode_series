from typing import List

# The following solution is easiest to come up with in real interview, but only works for 4 sum.
# For more general k-sum solution, see at the bottom
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                currTarget = target - (nums[i] + nums[j])
                while l < r:
                    twoSum = nums[l] + nums[r]
                    if twoSum == currTarget:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l + 1 < len(nums) and nums[l + 1] == nums[l]:
                            l += 1
                        l += 1
                        r -= 1
                    elif twoSum < currTarget:
                        while l + 1 < len(nums) and nums[l + 1] == nums[l]:
                            l += 1
                        l += 1
                    else:
                        while r - 1 >= 0 and nums[r - 1] == nums[r]:
                            r -= 1
                        r -= 1

        return ans


'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.findKSum(nums, target, 4, [])
        return self.ans

    def findKSum(self, nums: List[int], target: int, k: int, curr: List[int]):
        if len(nums) < k or k < 2 or target < nums[0] * k or target > nums[-1] * k:
            return
        
        if k == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum == target:
                    self.ans.append(curr + [nums[l], nums[r]])
                    while l + 1 < len(nums) and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    r -= 1
                elif twoSum < target:
                    while l + 1 < len(nums) and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                else:
                    while r - 1 >= 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
        else:
            for i in range(len(nums) - k + 1):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                self.findKSum(nums[i + 1:], target - nums[i], k - 1, curr + [nums[i]])
'''