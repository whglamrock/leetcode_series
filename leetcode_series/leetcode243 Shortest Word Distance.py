class Solution(object):
    def shortestDistance(self, words, word1, word2):
        size = len(words)
        index1, index2 = size, size
        ans = size

        for i in xrange(size):    # only one pointer
            if words[i] == word1:
                index1 = i
                ans = min(ans, abs(index1-index2))
            elif words[i] == word2:
                index2 = i
                ans = min(ans, abs(index1-index2))

        return ans

Sol = Solution()
print Sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"makes","coding")


