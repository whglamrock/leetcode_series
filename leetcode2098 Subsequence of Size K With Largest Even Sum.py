from typing import List


# 1) O(N * log(N)) sorting solution. no need to use dp which will take O(N * k).
# 2) we can also optimize this to O(N * log(k)) using heapq to store the k maximum values along with its index
# + keeping an index set to find the minOddToRemove, minEvenToRemove, max_even_to_add, max_odd_to_add but it's a bit
# of a overkill in real interview. Below solution is more practical.
class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)[::-1]
        firstKSum = sum(nums[:k])
        if firstKSum % 2 == 0:
            return firstKSum

        # at this point we know firstKSum is an odd number
        minOddToRemove, minEvenToRemove = None, None
        for num in nums[:k]:
            if num % 2:
                minOddToRemove = num
            else:
                minEvenToRemove = num

        max_even_to_add, max_odd_to_add = None, None
        for num in reversed(nums[k:]):
            if num % 2:
                max_odd_to_add = num
            else:
                max_even_to_add = num

        ans = -1
        if minOddToRemove is not None and max_even_to_add is not None:
            ans = max(ans, firstKSum - minOddToRemove + max_even_to_add)
        if minEvenToRemove is not None and max_odd_to_add is not None:
            ans = max(ans, firstKSum - minEvenToRemove + max_odd_to_add)

        return ans
