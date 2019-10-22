
from collections import defaultdict, Counter

# O(N) bucket sort solution, because the countToNums.keys() <= N numToCount.keys() <= N

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numToCount = Counter(nums)
        countToNums = defaultdict(list)
        for num in numToCount:
            countToNums[numToCount[num]].append(num)

        count = max(countToNums.keys())
        ans = []

        while k:
            if count in countToNums:
                for num in countToNums[count]:
                    k -= 1
                    ans.append(num)
                    if k == 0:
                        return ans
            count -= 1



print Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)

