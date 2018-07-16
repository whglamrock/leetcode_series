
# easy to understand and beats 100%

class Solution(object):
    def partitionLabels(self, S):

        letterToRange = {}
        for i, c in enumerate(S):
            letterToRange[c] = i

        ans = [-1]
        farthest = 0
        for i, c in enumerate(S):
            farthest = max(letterToRange[c], farthest)
            if farthest <= i:
                ans.append(i)

        res = []
        for j in xrange(1, len(ans)):
            res.append(ans[j] - ans[j - 1])

        return res



S = "ababcbacadefegdehijhklij"
print Solution().partitionLabels(S)