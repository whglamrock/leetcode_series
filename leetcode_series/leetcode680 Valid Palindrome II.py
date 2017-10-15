
class Solution(object):
    def validPalindrome(self, s):

        if s is None: return False
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
            l += 1
            r -= 1

        return True

    # need to consider 2 possibilities when (s[l - 1] == s[r] and s[l + 1] == s[r]):
    #   l += 1 or r -=1 could both work
    def isPalindrome(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

