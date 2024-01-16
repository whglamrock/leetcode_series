from typing import List

# O(1) space solution shouldn't be really required in real interview,
# see Boyer–Moore majority vote algorithm: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = nums[0]
        for i in range(len(nums)):
            if count == 0:
                majority = nums[i]
                count += 1
                continue

            if majority != nums[i]:
                count -= 1
            else:
                count += 1

        return majority


print(Solution().majorityElement([1, 2, 2, 1, 2, 1, 2, 1]))
