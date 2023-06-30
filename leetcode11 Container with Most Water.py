# O(N) two pointer solution:
# 1) we try different bottom length;
# 2) with each bottom length we use 2 pointers to find the highest height[i] & height[j]
# the reason to use greedy algorithm: because the bottom length is reducing, we need to keep
# the higher height in order to possibly make the new area (with bottom length - 1) to be bigger
# than the previous area.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        area = 0
        i, j = 0, len(height) - 1

        while i < j:
            newArea = min(height[i], height[j]) * (j - i)
            area = max(area, newArea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area


print(Solution().maxArea([1, 2, 3, 12, 1, 2, 14, 8]))
# tricky test case:
print(Solution().maxArea([1, 3, 2, 5, 25, 24, 5]))
