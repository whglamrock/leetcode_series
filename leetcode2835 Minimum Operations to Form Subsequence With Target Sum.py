from typing import List

# In second condition where num <= target we always take num to form the subsequence:
# 1) Any number's binary representation proves that any target can be summed by a distinct list of power of 2's.
# 2) You can easily prove that for any target number where 2 ^ n <= target < 2 ^ (n + 1). The binary representation of
# target WILL HAVE TO include 2 ^ n. E.g., target = 23 and its binary representation includes 16 (16 + 4 + 2 + 1).
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        numsSum = sum(nums)
        if numsSum < target:
            return -1

        nums.sort()
        ans = 0
        while target:
            num = nums.pop()
            if numsSum - num >= target:
                numsSum -= num
            # 1) numsSum < num + target < 2 * target; so target > numsSum // 2
            # 2) we can always take this number to form a subsequence
            elif num <= target:
                numsSum -= num
                target -= num
            else:
                nums.append(num // 2)
                nums.append(num // 2)
                ans += 1

        return ans
