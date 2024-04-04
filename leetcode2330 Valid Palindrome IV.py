
class Solution:
    def makePalindrome(self, s: str) -> bool:
        return self.isPalindrome(s, 0, len(s) - 1, 2)

    def isPalindrome(self, s: str, l: int, r: int, k: int) -> bool:
        i, j = l, r
        while i < j:
            # need to change one of them
            if s[i] != s[j]:
                if k <= 0:
                    return False
                return self.isPalindrome(s, i + 1, j - 1, k - 1)
            i += 1
            j -= 1

        return True
