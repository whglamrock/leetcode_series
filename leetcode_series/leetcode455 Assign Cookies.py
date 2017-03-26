
# Greedy sort solution

class Solution(object):
    def findContentChildren(self, g, s):

        g.sort()
        s.sort()
        i, j = 0, 0
        numofcontent = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                numofcontent += 1
                i += 1
                j += 1
            else:
                j += 1

        return numofcontent