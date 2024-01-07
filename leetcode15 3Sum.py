from collections import defaultdict
from typing import List

# O(N * N) solution that will definitely work in real interview
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        twoSumToIndexPairs = defaultdict(list)

        for j in range(1, len(nums)):
            for i in range(j):
                twoSum = nums[i] + nums[j]
                twoSumToIndexPairs[twoSum].append([i, j])

        ans = []
        tripletSet = set()
        for k in range(2, len(nums)):
            if -nums[k] in twoSumToIndexPairs:
                for i, j in twoSumToIndexPairs[-nums[k]]:
                    if j < k:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        tripletStr = ','.join([str(num) for num in triplet])
                        if tripletStr not in tripletSet:
                            ans.append([nums[i], nums[j], nums[k]])
                            tripletSet.add(tripletStr)

        return ans


print(Solution().threeSum([0, 0, 0]))
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 1, 1]))
