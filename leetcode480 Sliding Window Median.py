from sortedcontainers import SortedList
from typing import List

# remember this sortedcontainers library. The SortedList uses a balanced BST to store the values so insert
# and remove both takes O(log(k)). Also SortedList[index] is also O(log(k)) because each node knows how many
# nodes are in its subtree, so getting certain index value can be done by going downwards in the BST.
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()
        ans = []
        for i, num in enumerate(nums):
            window.add(num)
            # O(logK) because the sortedList is a balanced BST
            if len(window) > k:
                window.remove(nums[i - k])
            if i < k - 1:
                continue
            if k % 2:
                ans.append(window[k // 2])
            else:
                ans.append((window[k // 2] + window[k // 2 - 1]) / 2)

        return ans


print(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))


'''
from bisect import insort
from typing import List

# O(n * k) solution with python built-in bisect insort (insert into a sorted list, O(n) time).
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
'''
