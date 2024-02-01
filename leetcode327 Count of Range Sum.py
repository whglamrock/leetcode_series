from typing import List

# The most practical way to complete an O(NlogN) solution in real interview is using merge sort:
# 1) Use a helper mergeSort() method to sort each half; in the process of sorting each half,
# count the number of ranges that completely in this half
# 2) For the case when range[0] in left half and range[1] in right half: iterate the left half,
# and look for any satisfiable range[1] in right half
# 3) See explanation: https://discuss.leetcode.com/topic/33770/short-simple-o-n-log-n
class Solution(object):
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        # we merge sort the prefixSum array (l inclusive, r exclusive)
        def mergeSort(l, r):
            m = (l + r) // 2
            # in this recursion, there is only 1 prefixSum element which is meaningless
            if m == l:
                return 0

            # when ranges are completely in either left or right half
            count = mergeSort(l, m) + mergeSort(m, r)

            # when range[0] in left half, range[1] in right half
            i, j = m, m
            for left in prefixSum[l:m]:
                while i < r and prefixSum[i] - left < lower:
                    i += 1
                while j < r and prefixSum[j] - left <= upper:
                    j += 1
                count += j - i

            # a lazy way of doing this but can be achieved by O(N) with Python TimSort, because the left & right half
            # are already sorted. N = r - l, not the length of the original nums array
            prefixSum[l:r] = sorted(prefixSum[l:r])
            return count

        return mergeSort(0, len(prefixSum))


print(Solution().countRangeSum([-2, 5, -1], -2, 2))
