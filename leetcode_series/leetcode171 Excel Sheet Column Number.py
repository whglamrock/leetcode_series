
class Solution(object):
    def titleToNumber(self, s):

        num = 0
        for i in range(len(s)):
            num = num * 26 + (ord(s[i])-64)

        return num



a = 'ABB'
Sol = Solution()
print Sol.titleToNumber('ZZ')


