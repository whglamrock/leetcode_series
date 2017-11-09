
# O(nlogn) solution.
# My idea explanation: https://discuss.leetcode.com/topic/62048/easy-to-understand-python-solution

class Solution(object):
    def isReflected(self, points):

        if (not points):
            return True

        dick = {}
        sumx = 0
        lenwithoutdup = 0
        for point in points:
            if point[1] not in dick:
                dick[point[1]] = {point[0]}
                sumx += point[0]
                lenwithoutdup += 1
            else:
                if point[0] not in dick[point[1]]:
                    dick[point[1]].add(point[0])
                    sumx += point[0]
                    lenwithoutdup += 1

        #print sumx, lenwithoutdup
        avgx = float(sumx)/lenwithoutdup
        for item in dick:
            lst = list(dick[item])
            lst.sort()
            i, j = 0, len(lst)-1
            while i <= j:
                #print lst[i], avgx, lst[j]
                if lst[i] - avgx != avgx - lst[j]:
                    return False
                i += 1
                j -= 1

        return True



Sol = Solution()
points = [[-16,1], [16,1], [16,1]]
print Sol.isReflected(points)
