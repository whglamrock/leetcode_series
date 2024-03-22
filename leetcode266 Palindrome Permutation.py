from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        charCount = Counter(s)
        oddCharCount = 0
        for count in charCount.values():
            if count % 2:
                oddCharCount += 1

        return oddCharCount <= 1
