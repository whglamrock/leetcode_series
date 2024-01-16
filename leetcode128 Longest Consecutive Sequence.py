from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        numsSet = set(nums)
        ans = 0
        for num in nums:
            if num in visited:
                continue

            count = 0
            tmp = num
            # go smaller
            while num in numsSet and num not in visited:
                visited.add(num)
                num -= 1
                count += 1

            num = tmp + 1
            # go bigger
            while num in numsSet and num not in visited:
                visited.add(num)
                num += 1
                count += 1

            ans = max(ans, count)

        return ans


print(Solution().longestConsecutive([100, 1, 3, 4, 2, 6, 5, 8]))
