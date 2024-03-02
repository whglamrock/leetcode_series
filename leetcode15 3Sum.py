from typing import List

# a naive hashmap solution can't achieve O(N ^ 2), you will have to use two pointers.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = set()
        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    triplets.add((nums[l], nums[r], nums[i]))
                    l += 1
                    r -= 1

        ans = []
        for triplet in triplets:
            ans.append(list(triplet))
        return ans


print(Solution().threeSum([0, 0, 0]))
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 1, 1]))
