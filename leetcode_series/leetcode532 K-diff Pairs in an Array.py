
from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):

        if not nums or k < 0:
            return 0

        dic = Counter(nums)
        ans = set()
        if k == 0:
            count = 0
            for key in dic:
                if dic[key] > 1:
                   count += 1
            return count

        for key in dic:
            if key + k in dic:
                ans.add((key, key + k))
            if key - k in dic:
                ans.add((key - k, key))

        return len(ans)



Sol = Solution()
nums = [1, 2, 3, 4, 5]
k = 1
print Sol.findPairs(nums, k)
