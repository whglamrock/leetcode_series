
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        currSubStr = []
        ans = []

        for c in s:
            if c != ' ':
                currSubStr.append(c)
            else:
                for reversedChar in currSubStr[::-1]:
                    ans.append(reversedChar)
                ans.append(' ')
                currSubStr = []

        if currSubStr:
            for reversedChar in currSubStr[::-1]:
                ans.append(reversedChar)

        return ''.join(ans)



Sol = Solution()
s = "Let's take LeetCode contest"
print Sol.reverseWords(s)
