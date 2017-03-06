class Solution:
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)  # cursum means the maximum sum of subarray that ends with
            # current element
            maxSum = max(maxSum, curSum)  # mark the ever existent maximum sum

        return maxSum


nums = [-2,-1,-1,-1,7,4,-3,-4,-5,5]
Sol = Solution()
print Sol.maxSubArray(nums)
