
# there is no way to do better than O(nlogn) time complexity

from copy import deepcopy
class Solution(object):
    def findRelativeRanks(self, nums):

        numscopy = deepcopy(nums)
        numscopy.sort()
        numscopy.reverse()

        rank = {}
        for i, num in enumerate(numscopy):
            rank[num] = i + 1

        ans = []
        for num in nums:
            numrank = rank[num]
            if numrank == 1:
                ans.append("Gold Medal")
            elif numrank == 2:
                ans.append("Silver Medal")
            elif numrank == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(numrank))

        return ans