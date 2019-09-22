
# O(N) two pointer solution
# At some point assume we have height[i] < height[j]); if we decrease the right index, all new areas will smaller
    # the one formed by  height[i] & height[j]. But increasing height[i] we can possibly find better solution

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



print Solution().maxArea([1, 2, 3, 12, 1, 2, 14, 8])



