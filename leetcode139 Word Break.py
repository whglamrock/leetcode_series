
# O(N^2) classic dp solution.

class Solution(object):
    def wordBreak(self, s, wordDict):

        # only need to check the wordDict because s is non-empty
        if not wordDict: return False

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        wordDict = set(wordDict)

        for i in xrange(len(s) + 1):
            for j in xrange(i):
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1
                # once we know s[:i] is breakable, we don't need other sub-solutions
                if dp[i] == 1: break

        return dp[-1] == 1



'''
# DFS with memoization solution:

class Solution(object):
    def wordBreak(self, s, wordDict):

        if not wordDict:
            return False    # because s is non-empty

        wordDict = set(wordDict)
        self.memo = {}

        def dfs(substring, wordDict):

            if not substring:
                return True
            if substring in self.memo:
                return self.memo[substring]
            for i in xrange(1, len(substring) + 1):
                if substring[:i] in wordDict:
                    if dfs(substring[i:], wordDict):
                        return True
                    else:
                        self.memo[substring[i:]] = False

            self.memo[substring] = False
            return False

        return dfs(s, wordDict)
'''
