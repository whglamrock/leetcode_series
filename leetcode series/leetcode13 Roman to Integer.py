'''
O(n) time complexity, O(1) time space complexity
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        def judge(zifu):
            if zifu == 'I':
                return 1
            elif zifu == 'V':
                return 5
            elif zifu == 'X':
                return 10
            elif zifu == 'L':
                return 50
            elif zifu == 'C':
                return 100
            elif zifu == 'D':
                return 500
            elif zifu == 'M':
                return 1000

        if len(s) == 1:
            return judge(s[0])

        i = 0
        ans = 0

        while i < len(s)-1:
            if judge(s[i]) < judge(s[i+1]):
                ans += judge(s[i+1])-judge(s[i])
                i += 2
                if i == len(s)-1:
                    ans += judge(s[i])
            else:
                ans += judge(s[i])
                i += 1
                if i == len(s)-1:
                    ans += judge(s[i])

        return ans


a = 'D'
Sol = Solution()
print Sol.romanToInt(a)






