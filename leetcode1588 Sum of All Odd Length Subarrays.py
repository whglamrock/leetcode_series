from typing import List


# O(N) idea is using dp: we get the sum of even/odd length subarray that ends at arr[i].
# The numOfEvenSubarray, numOfOddSubarrays variables are optional: we should be able to calculate them using index i.
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        numOfOddSubarrays, numOfEvenSubarray = 1, 0
        oddSum, evenSum = arr[0], 0
        ans = oddSum
        for i in range(1, len(arr)):
            num = arr[i]
            oddSum, evenSum = evenSum + numOfEvenSubarray * num + num, oddSum + numOfOddSubarrays * num
            ans += oddSum
            numOfEvenSubarray, numOfOddSubarrays = numOfOddSubarrays, numOfEvenSubarray + 1

        return ans
