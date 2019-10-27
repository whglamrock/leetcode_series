
from collections import defaultdict

# build a prefix to words mapping. because each word has the same length, we try with every word as
# the first line of the output.
# when we add word, we calculate the prefix (the prefix ends with the letter at diagnol of the output matrix)

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words:
            return []

        n = len(words[0])
        prefixToWords = defaultdict(list)
        for word in words:
            for i in xrange(1, n + 1):
                prefixToWords[word[:i]].append(word)

        ans = []
        for word in words:
            self.helper(prefixToWords, [word], n, ans)

        return ans

    # n is the length of each word
    def helper(self, prefixToWords, curr, n, ans):
        if len(curr) == n:
            ans.append(curr)
            return

        m = len(curr)
        prefix = ''
        for i in xrange(m):
            prefix += curr[i][m]

        for word in prefixToWords[prefix]:
            self.helper(prefixToWords, curr + [word], n, ans)



print Solution().wordSquares(["abat", "baba", "atan", "atal"])
print Solution().wordSquares(["area", "lead", "wall", "lady", "ball"])
