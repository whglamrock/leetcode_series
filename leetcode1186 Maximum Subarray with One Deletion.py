from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # max sub array sum which starts at arr[i]
        maxSubArraySumStart = [0 for _ in range(len(arr))]
        # max sub array sum which ends at arr[i]
        maxSubArraySumEnd = [0 for _ in range(len(arr))]
        maxSubArraySumStart[-1] = arr[-1]
        maxSubArraySumEnd[0] = arr[0]
        n = len(arr)

        for i in range(1, n):
            if maxSubArraySumEnd[i - 1] >= 0:
                maxSubArraySumEnd[i] = maxSubArraySumEnd[i - 1] + arr[i]
            else:
                maxSubArraySumEnd[i] = arr[i]

        for i in range(n - 2, -1, -1):
            if maxSubArraySumStart[i + 1] >= 0:
                maxSubArraySumStart[i] = maxSubArraySumStart[i + 1] + arr[i]
            else:
                maxSubArraySumStart[i] = arr[i]

        ans = -2147483648
        for i, num in enumerate(arr):
            # maxSubArraySum only with arr[i] optionally deleted
            maxSubArraySum = 0
            leftSideUsed = False
            rightSideUsed = False
            # when maxSubArraySumEnd[i - 1] == 0 we still "use" the left side
            # because it will allow arr[i] to be deleted if arr[i] < 0
            if i > 0 and maxSubArraySumEnd[i - 1] >= 0:
                maxSubArraySum += maxSubArraySumEnd[i - 1]
                leftSideUsed = True
            if i + 1 < n and maxSubArraySumStart[i + 1] >= 0:
                maxSubArraySum += maxSubArraySumStart[i + 1]
                rightSideUsed = True

            # don't delete the number if it's > 0
            if num >= 0:
                maxSubArraySum += num
            else:
                # cannot be an empty subarray
                if not leftSideUsed and not rightSideUsed:
                    maxSubArraySum += num
            ans = max(ans, maxSubArraySum)

        return ans


print(Solution().maximumSum([1, -2, 0, 3]))
print(Solution().maximumSum([1, -2, -2, 3]))
print(Solution().maximumSum([-1, -1, -1, -1]))
