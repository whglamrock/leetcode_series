
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelCount = 0
        l = 0
        ans = 0
        for r, char in enumerate(s):
            if char in 'aeiou':
                vowelCount += 1
            while r - l + 1 > k:
                if s[l] in 'aeiou':
                    vowelCount -= 1
                l += 1
            ans = max(ans, vowelCount)

        return ans
