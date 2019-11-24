
# Guaranteed O(N^2) DP solution

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        # the farthest step can only be n - 1, in which case the step length has to keep increasing
        # dp[i][j] means at stones[i] whether we can jump step j
        dp = [[False for j in xrange(n)] for i in xrange(n)]
        dp[0][1] = True

        for i in xrange(1, n):
            for j in xrange(i):
                lastStep = stones[i] - stones[j]
                if lastStep <= 0 or lastStep >= n or not dp[j][lastStep]:
                    continue
                dp[i][lastStep] = True
                if lastStep - 1 > 0:
                    dp[i][lastStep - 1] = True
                if lastStep + 1 < n:
                    dp[i][lastStep + 1] = True

        for j in xrange(n):
            if dp[-1][j] == True:
                return True
        return False



print Solution().canCross([0, 1, 2, 4, 5, 6, 7, 9, 10, 11, 13])
print Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11])



'''
# DFS & memoization solution, which actually runs much faster than dp

class Solution(object):
    def canCross(self, stones):

        # stones list will have at least 2 stones
        if stones[1] != 1:
            return False

        return self.dfs(stones[1], 1, stones[-1], set(stones), set())

    def dfs(self, currStone, lastStep, destination, stonesSet, memo):

        if (currStone, lastStep) in memo:
            return False
        if currStone not in stonesSet or currStone == 0:
            return False

        if currStone == destination:
            return True

        steps = [lastStep, lastStep + 1]
        if lastStep - 1 > 0:
            steps.append(lastStep - 1)

        for step in steps:
            if self.dfs(currStone + step, step, destination, stonesSet, memo):
                return True

        memo.add((currStone, lastStep))
        return False
'''