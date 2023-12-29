from typing import List

# greedy algorithm solution
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i][i] == '1':
                ans.append('0')
            else:
                ans.append('1')

        return ''.join(ans)


print(Solution().findDifferentBinaryString(["00", "01"]))
print(Solution().findDifferentBinaryString(["111", "011", "001"]))
