
# A very easy "hard" question.
# idea: sliding window; O(N) time, O(1) space

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):

        window = {}
        curl = 0  # the left bound of window
        curlen = 0  # the current size of the window
        maxlen = 0
        for i in xrange(len(s)):
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1
            curlen += 1
            if len(window) > 2:
                while len(window) > 2:
                    window[s[curl]] -= 1
                    curlen -= 1
                    if window[s[curl]] == 0:
                        del window[s[curl]]
                    curl += 1
            maxlen = max(maxlen, curlen)

        return maxlen