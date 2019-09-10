
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.dfs(s, wordDict, {})

    # use substringToWordBreak as a memo/backtracking to store the work break for visited substrings, which largely
        # saves time for tricky case like "aaaa...", ["a", 'aa', "aaa", ...]
    def dfs(self, s, wordDict, substringToWordBreak):

        if s in substringToWordBreak:
            return substringToWordBreak[s]

        # base case when all words in this recursion path are in wordDict
        if len(s) == 0:
            return ['']

        res = []
        for word in wordDict:   # wordDict has no duplicates
            if s.startswith(word):
                wordBreakForSuffix = self.dfs(s[len(word):], wordDict, substringToWordBreak)
                for item in wordBreakForSuffix:
                    # item can be ''
                    res.append((word + ' ' + item).strip())

        substringToWordBreak[s] = res
        return res



print Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog", "an", "ddog"])
print Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
print Solution().wordBreak("aaaaaaaa", ["a", 'aa', "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"])