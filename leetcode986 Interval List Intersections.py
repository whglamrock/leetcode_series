
# write the calculateIntersection method first, then the logic will be pretty clear
# note that interval1, interval1 cannot be empty

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        edges = []
        i, j = 0, 0
        m, n = len(A), len(B)

        while i < m and j < n:
            intersection = self.calculateIntersection(A[i], B[j])
            if intersection:
                edges.append(intersection)
            # we proceed for the smaller interval to make sure we don't miss intersections
            if A[i][1] < B[j][1]:
                i += 1
            else:   # when A[i][1] == B[j][1], it doesn't matter which one of [A, B] proceeds
                j += 1

        return edges

    def calculateIntersection(self, interval1, interval2):
        if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
            return []
        if interval1[1] == interval2[0]:
            return [interval1[1], interval1[1]]
        if interval2[1] == interval1[0]:
            return [interval2[1], interval2[1]]
        positions = sorted(interval1 + interval2)
        return [positions[1], positions[2]]



print Solution().intervalIntersection(A=[[0,2],[5,10],[13,23],[24,25]], B=[[1,5],[8,12],[15,24],[25,26]])
