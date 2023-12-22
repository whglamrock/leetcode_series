
class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        ans = []
        highest = -1
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > highest:
                ans.append(i)
                highest = heights[i]

        return ans[::-1]


print(Solution().findBuildings([4, 3, 2, 1]))
print(Solution().findBuildings([4, 2, 3, 1]))
print(Solution().findBuildings([1, 3, 2, 4]))
