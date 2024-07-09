from typing import List


# Remember the below solution. Since nums[i] is an integer we just need to maintain a max & min product that ends at
# each num[i]. Suppose we have a subarray without 0, the max abs value of a product must be the product of the entire subarray.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum, minimum = nums[0], nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                maximum, minimum = minimum, maximum
            # this way, we can get rid of 0 after the pass through the 0 elements
            maximum = max(nums[i], nums[i] * maximum)
            minimum = min(nums[i], nums[i] * minimum)
            ans = max(ans, maximum)

        return ans


print(Solution().maxProduct([-9, -4, 2, 7, -3, 8, 3]))
