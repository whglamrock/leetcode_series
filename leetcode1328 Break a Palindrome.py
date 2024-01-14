
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''

        firstNonACharInFirstHalf = None
        # notice here we don't care about middle char for strings like 'aabaa'
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                firstNonACharInFirstHalf = palindrome[i]
                break

        if firstNonACharInFirstHalf is not None:
            return palindrome[:i] + 'a' + palindrome[i + 1:]

        # here all chars are a.
        return palindrome[:len(palindrome) - 1] + 'b'


print(Solution().breakPalindrome("abccba"))
print(Solution().breakPalindrome("aba"))
print(Solution().breakPalindrome("a"))
print(Solution().breakPalindrome("b"))
print(Solution().breakPalindrome("aaabaaa"))
print(Solution().breakPalindrome("aaaccaaa"))
