
# O(NlogN) solution by sorting.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort()
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                if stack[-1][1] >= interval[0]:
                    lastInterval = stack.pop()
                    stack.append([lastInterval[0], max(interval[1], lastInterval[1])])
                else:
                    stack.append(interval)

        return stack



print Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
print Solution().merge([[5, 10], [1, 3]])
