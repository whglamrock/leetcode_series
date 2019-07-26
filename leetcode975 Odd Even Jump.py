
# idea from: https://leetcode.com/problems/odd-even-jump/discuss/217981/JavaC%2B%2BPython-DP-idea-Using-TreeMap-or-Stack

class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        # using 0 as initial value covers the corner case when len(A) == 1
        nextHigher, nextLower = [0] * n, [0] * n

        stack = []
        sortedAscending = [[i, a] for i, a in enumerate(A)]
        # if multiple elements of A are same value, we want the first i to be
            # used/compared first. e.g., 3, 6, 6, nextHigher[0] should be 1 not 2
            # so i == 1 should come before i == 2 in the for loop
        sortedAscending.sort(key=lambda x: (x[1], x[0]))
        for i, a in sortedAscending:
            # stack[-1] < i and previous a < current a
            while stack and stack[-1] < i:
                nextHigher[stack.pop()] = i
            stack.append(i)

        stack = []
        sortedDecending = [[i, a] for i, a in enumerate(A)]
        sortedDecending.sort(key=lambda x: (-x[1], x[0]))
        for i, a in sortedDecending:
            # stack[-1] < i and previous a > current a
            while stack and stack[-1] < i:
                nextLower[stack.pop()] = i
            stack.append(i)

        # the dp idea: if higher[i] == 1, then we can jump higher at i
            # and will be able to reach the end
        higher, lower = [0] * n, [0] * n
        higher[-1], lower[-1] = 1, 1
        for i in xrange(n - 2, -1, -1):
            higher[i] = lower[nextHigher[i]]
            lower[i] = higher[nextLower[i]]

        # any 1 step route will be a higher jump;
        # any multi step route's first step will be higher jump
        return sum(higher)



print Solution().oddEvenJumps(A=[10,13,12,14,15])


