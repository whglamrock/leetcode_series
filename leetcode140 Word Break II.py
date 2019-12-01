
# it's easiest to think of DFS & memoization:
    # step1: define what DFS function should return
    # step2: define what is the key & value of the memo (ideally the value should be in the same type as DFS return)
    # step3: so we know what we should return as base case

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if not s:
            return ['']

        if s in memo:
            return memo[s]

        res = []
        for word in wordDict:
            if s.startswith(word):
                wordBreakOfSuffix = self.dfs(s[len(word):], wordDict, memo)
                for item in wordBreakOfSuffix:
                    # don't forget to strip() in case item == ''
                    res.append((word + ' ' + item).strip())

        memo[s] = res
        return res



print Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog", "an", "ddog"])
print Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
print Solution().wordBreak("aaaaaaaa", ["a", 'aa', "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"])