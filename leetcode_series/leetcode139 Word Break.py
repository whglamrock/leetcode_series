
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

        self.dic = {}
        worddic = set(wordDict)

        def helper(currs, worddic):
            if not currs:
                return True
            if currs in self.dic:
                return self.dic[currs]
            for i in xrange(1, len(currs) + 1):
                if currs[:i] in worddic:
                    if helper(currs[i:], worddic):
                        return True
                    else:
                        self.dic[currs[i:]] = False
            self.dic[currs] = False
            return False

        return helper(s, worddic)
'''
