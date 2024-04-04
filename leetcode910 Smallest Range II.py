from typing import List

# See explanation: https://leetcode.com/problems/smallest-range-ii/solutions/173495/actual-explanation-for-people-who-don-t-understand-i-hope/
# Intuition:
# 0) sort the nums. The absolute max range is nums[-1] - nums[0]
# 1) looping through 1 to n - 1, consider nums[i] as the maximum, then nums[i] must add K (otherwise even if all
# nums[i + 1:] all minus K, nums[i + 1:] will be bigger than nums[i]; remember we have to either add or minus K)
# if we don't add K to nums[i], then all nums[i:] will have to -K, which makes all nums[i] -K which is pointless.
# 2) all nums[i + 1:] will have to minus K, because we added K to nums[i]
# 3) all nums[i:] will have to add K, otherwise we will make things worse
# 4) Thus, if we try to make nums[i] the maximum (by adding K), we know how to calculate the max & min of the modified
# array:
#  4a) the maximum will be the max(lastNum - K, nums[i] + K) because all nums[:i] < nums[i] and all we -K for nums[i + 1:]
#  4b) the min will be min(firstNum + K, nums[i + 1] - K)
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            maxI = max(nums[i] + k, nums[-1] - k)
            minI = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, maxI - minI)

        return ans
