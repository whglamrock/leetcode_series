from typing import List

# binary search solution
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        k -= arr[0] - 1
        if len(arr) == 1:
            return arr[0] + k

        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r + 1) // 2
            # total num of missing numbers in the left are: nums[m] - nums[l] - (r - l)
            if arr[m] - arr[l] - (m - l) >= k:
                r = m - 1
            else:
                k -= arr[m] - arr[l] - (m - l)
                l = m

        # exit condition has to be l == r
        return arr[l] + k


print(Solution().findKthPositive(arr=[2, 3, 4, 7, 11], k=5))
print(Solution().findKthPositive(arr=[1, 2, 3, 4], k=2))
