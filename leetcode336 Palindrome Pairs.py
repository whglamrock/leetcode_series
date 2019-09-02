
# O(n * w^2) solution. No need to use dp to calculate if the prefix/suffix is palindrome (no time improvement)

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if not words:
            return []

        wordToIndex = {word: i for i, word in enumerate(words)}
        ansSet = set()

        for i, word in enumerate(words):
            if not word:
                continue
            n = len(word)
            for j in xrange(n + 1):
                prefix, suffix = word[:j], word[j:]
                if self.isPalindrome(prefix):
                    wordToPair = suffix[::-1]
                    # don't forget to to make sure wordToIndex[wordToPair] != i
                    if wordToPair in wordToIndex and wordToIndex[wordToPair] != i:
                        ansSet.add((wordToIndex[wordToPair], i))
                if self.isPalindrome(suffix):
                    wordToPair = prefix[::-1]
                    if wordToPair in wordToIndex and wordToIndex[wordToPair] != i:
                        ansSet.add((i, wordToIndex[wordToPair]))

        ans = []
        for item in ansSet:
            ans.append(list(item))
        return ans

    def isPalindrome(self, word):
        return word == word[::-1]



print Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
print Solution().palindromePairs(["bb","bababab","baab","abaabaa","aaba","","bbaa","aba","baa","b"])














