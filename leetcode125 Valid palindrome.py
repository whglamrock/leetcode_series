class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for char in s:
            if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                chars.append(char.lower())
            elif char in 'abcdefghijklmnopqrstuvwxyz' or char.isdigit():
                chars.append(char)

        return chars == chars[::-1]
