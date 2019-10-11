
# remember the built-in check function: isalpha(), isalnum(), islower, isupper(), isdigit(),
    # and the lower and upper function.

# O(1) space solution

class Solution(object):
    def isPalindrome(self, s):

        if s == None:
            return False
        if not s:
            return True

        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True



print Solution().isPalindrome('WGlGlw')
print Solution().isPalindrome('0P')
print Solution().isPalindrome('.,')
print Solution().isPalindrome('A man, a plan, a canal: Panama')
