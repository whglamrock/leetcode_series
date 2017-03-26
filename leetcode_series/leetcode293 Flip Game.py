
# s[x:y] operator still have time complexity compared with for loop method.
# space complexity doesn't need to be considered in this case, cuz the s[:] operator will have, and using for
# loop to build a new string corresponding to the current state still will use memory.

class Solution(object):
    def generatePossibleNextMoves(self, s):

        ans = []
        for i in xrange(len(s)-1):
            if s[i] == s[i+1] == '+':
                ans.append(s[:i]+'--'+s[i+2:])

        return ans

# no need to test
