
class Solution(object):
    def countAndSay(self, n):

        if n <= 0:
            return ''
        if n == 1:
            return '1'
        if n == 2:
            return '11'

        ans = '11'
        for i in xrange(2, n):
            newseq = ''
            count = 0
            for j in xrange(len(ans)):
                if j == 0 or (j > 0 and ans[j] == ans[j - 1]):
                    count += 1
                else:
                    newseq += str(count) + ans[j - 1]
                    count = 1
            newseq += str(count) + ans[-1]
            ans = newseq

        return ans



a = Solution()
b = a.countAndSay(7)
print b








