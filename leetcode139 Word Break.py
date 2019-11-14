
# DP solution, not necessarily O(N^2) because s[j:i] substring takes time to build.
# In real interview, it will be impressive to mention the Trie solution and its potential improvements/tradeOff

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False

        wordDict = set(wordDict)
        n = len(s)
        # dp[i] means whether s[:i] can be constructed by words in wordDict
        dp = [False] * (n + 1)
        dp[0] = True

        for i in xrange(1, n + 1):
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]



'''
# DFS with memoization solution. 
# May be faster than the DP idea because it will return True when it finds any valid work break

class Solution(object):
    def wordBreak(self, s, wordDict):

        if not wordDict:
            return False
        
        wordDict = set(wordDict)
        return self.dfs(s, wordDict, {})
        
    def dfs(self, subString, wordDict, memo):
        if not subString:
            return True
        if subString in memo:
            return memo[subString]
        
        for i in xrange(1, len(subString) + 1):
            if subString[:i] in wordDict:
                newSubString = subString[i:]
                if self.dfs(newSubString, wordDict, memo):
                    memo[subString] = True
                    return True
        
        memo[subString] = False
        return False
'''
