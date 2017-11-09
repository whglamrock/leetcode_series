
# remember the built-in check function: isalpha(), isalnum(), islower, isupper(), isdigit(),
#   also the lower and upper function

class Solution(object):
    def isPalindrome(self, s):

        if s == None: return False  # the case when s is empty is included in the following while loop

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True



a = Solution()
b = 'WGlGl'
print a.isPalindrome(b)

