
from collections import Counter
from bisect import bisect_right

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        wordF = []
        for word in words:
            wordF.append(self.f(word))
        wordF.sort()

        ans = []
        for query in queries:
            f_q = self.f(query)
            # insert_pos is the number of elements in wordF that <= f_q
            insert_pos = bisect_right(wordF, f_q)
            ans.append(len(wordF) - insert_pos)

        return ans

    def f(self, word):
        charCount = Counter(word)
        smallestChar = 'z'
        for char in charCount:
            smallestChar = min(smallestChar, char)

        return charCount[smallestChar]



print Solution().numSmallerByFrequency(["bbb","cc"], ["a","aa","aaa","aaaa"])