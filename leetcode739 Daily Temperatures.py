
# typical decreasing stack question

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return []

        stack = []
        n = len(T)
        ans = [0] * n

        for i in xrange(n):
            while stack and T[i] > T[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)

        while stack:
            ans[stack.pop()] = 0

        return ans



print Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])