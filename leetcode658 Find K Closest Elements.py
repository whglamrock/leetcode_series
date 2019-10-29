
# Draw graph on paper to understand what "x - arr[m] > arr[m + k] - x" means
# See explanation in: https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) / 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            # including the good case where x - arr[m] == arr[m + k] - x
                # so we make r = mid, not r = mid - 1
            # Also final goal is to make l == r.
            else:
                r = m

        return arr[l:l + k]



print Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3)
