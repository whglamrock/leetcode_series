# classic DFS
class Solution:
    def subsetsWithDup(self, S):

        if (not S): return []
        S.sort()
        ans = []

        def helper(last, lastindex):
            original = len(ans)
            for i in xrange(lastindex+1, len(S)):
                if i > lastindex+1 and S[i] == S[i-1]:  # memorize this if condition (deal with duplicates).
                    continue
                ans.append(last+[S[i]])
                helper(last+[S[i]], i)
            if len(ans) == original:
                return

        helper([], -1)
        ans.append([])
        return ans


Sol = Solution()
S = [1,2,2,2,3,3,4]
print Sol.subsetsWithDup(S)


'''
# optimal solution without extra space
class Solution:
    def subsetsWithDup(self, S):

        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:  # let's assume S = [1,2,2,2,3,3,4]
                l = len(res)
            for j in range(len(res) - l, len(res)):    # go through for loop of i & j to find delicacy of this line
                res.append(res[j] + [S[i]])  # for every s[i], add it to all existent res[j] to form new 'res[j]'.
        return res

# the most important trick is the move of j's range. Write down every for loop with above test case to find out.
'''