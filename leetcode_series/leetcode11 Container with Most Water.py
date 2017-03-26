
'''
    Two pointers are set: i starts from 0, j starts from len(height)-1; let's say height[i] < height[j]).
    Should we move i or j?
    -- if j, no matter what height[j-1] is, the new area will be less than the previsou one.
    -- if i, when height[i+1] <= height[i], area decrease ; but if height[i+1] > height[i], the area
       could increase
'''

class Solution(object):
    def maxArea(self, height):

        i = 0
        j = len(height)-1
        area = min(height[i],height[j])*(j-i)

        while i < j:
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
            if min(height[i],height[j])*(j-i) > area:
                    area = min(height[i],height[j])*(j-i)

        return area



a = [1,2,3,12,1,2,14,8]
Sol = Solution()
print Sol.maxArea(a)



