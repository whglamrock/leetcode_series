from typing import List

# for k = 3 and [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1] -> [5,6,7,4,3,2,1] -> [5,6,7,1,2,3,4]
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # for k > n use case, needs to clarify in the interview
        k %= n

        nums.reverse()
        # reverse the first k
        for i in range(k // 2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
        # reverse the rest
        for j in range((n - k) // 2):
            nums[k + j], nums[n - 1 - j] = nums[n - 1 - j], nums[k + j]


nums1 = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums1, 3)
print(nums1)
nums2 = [-1]
Solution().rotate(nums2, 2)
print(nums2)
nums3 = [1, 2]
Solution().rotate(nums3, 3)
print(nums3)
nums4 = [-1, 3, 4, 5]
Solution().rotate(nums4, 10)
print(nums4)
