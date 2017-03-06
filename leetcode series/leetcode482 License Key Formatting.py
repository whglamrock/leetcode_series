class Solution(object):
    def licenseKeyFormatting(self, S, K):

        # the upper() and replace() both takes O(n) time complexity
        S = S.upper().replace('-', '')
        n = len(S)

        ans = []
        start = n % K
        for i in xrange(start):
            ans.append(S[i])
        if ans:
            ans.append('-')

        count = 0
        for i in xrange(start, n):
            count += 1
            ans.append(S[i])
            if count == K:
                count = 0
                ans.append('-')

        if ans: ans.pop()
        return ''.join(ans)