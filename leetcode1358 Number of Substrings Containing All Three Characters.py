from collections import defaultdict

# sliding window solution
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # find the shortest substring that starts with s[l] which contain all of a, b, c
        window = defaultdict(int)
        l, r = 0, 0
        numOfSubstr = 0
        while r < len(s):
            # find the right index;
            # r will be moved rightward by one extra char so the substring is actually s[l:r]
            while r < len(s) and (window['a'] == 0 or window['b'] == 0 or window['c'] == 0):
                window[s[r]] += 1
                r += 1
            # it means we can't find such string that starts with s[l]
            if window['a'] == 0 or window['b'] == 0 or window['c'] == 0:
                break

            # move the left index, find all substrings within s[l:r]
            while l < r - 2 and window['a'] > 0 and window['b'] > 0 and window['c'] > 0:
                numOfSubstr += len(s) - r + 1
                window[s[l]] -= 1
                l += 1

        return numOfSubstr






