from bisect import insort
from typing import List

# O(n * k) solution with python built-in bisect insort (insert into a sorted list, O(n) time), most practical in real interview.
# The 2 heap O(n * log(k)) solution requires lazy removal for out of bound elements, which are super error-prone.
class Solution(object):
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans, window = [], []
        for i in range(len(nums)):
            if i >= k:
                window.remove(nums[i - k])

            # python bisect insort can achieve O(n) time while maintaining the sorted order
            insort(window, nums[i])
            if i >= k - 1:
                if k % 2 == 0:
                    ans.append((window[k // 2 - 1] + window[k // 2]) / 2)
                else:
                    ans.append(window[k // 2])

        return ans


print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
