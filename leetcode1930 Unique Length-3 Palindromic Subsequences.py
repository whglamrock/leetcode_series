from collections import defaultdict, Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        prefixCharCount, suffixCharCount = defaultdict(int), Counter(s)
        prefixCharCount[s[0]] += 1
        suffixCharCount[s[0]] -= 1
        if not suffixCharCount[s[0]]:
            del suffixCharCount[s[0]]
        suffixCharCount[s[1]] -= 1
        if not suffixCharCount[s[1]]:
            del suffixCharCount[s[1]]

        ans = set()
        for i in range(1, len(s) - 1):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char in prefixCharCount and char in suffixCharCount:
                    ans.add(char + s[i] + char)
            prefixCharCount[s[i]] += 1
            suffixCharCount[s[i + 1]] -= 1
            if not suffixCharCount[s[i + 1]]:
                del suffixCharCount[s[i + 1]]

        return len(ans)
