
class Solution(object):
    def palindromePairs(self, words):

        ans = set()
        res = []
        wordict = {word: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            for j in xrange(len(word) + 1):
                tmp1 = word[:j]
                tmp2 = word[j:]
                if tmp1[::-1] in wordict and wordict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                    ans.add((i,wordict[tmp1[::-1]]))
                # ans is a set, to avoid duplicates like "abc" & "cba".
                if tmp2[::-1] in wordict and wordict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                    ans.add((wordict[tmp2[::-1]],i))

        for item in ans:
            res.append(list(item))
        return res



Sol = Solution()
words = ["abcd", "dcba", "lls", "s", "sssll"]
print Sol.palindromePairs(words)















