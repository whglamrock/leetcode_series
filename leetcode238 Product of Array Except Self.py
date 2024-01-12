from typing import List

# Note: the output doesn't count as extra space. If the question asks for not using division, it's close to hard level
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        suffixProduct = nums[-1]
        for i in range(n - 2, -1, -1):
            ans[i] *= suffixProduct
            suffixProduct *= nums[i]

        return ans


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([1, 2, 3, 0]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
