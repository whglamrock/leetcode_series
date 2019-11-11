
# KMP algorithm.
# Theory from youtube: https://www.youtube.com/watch?v=GTJr8OvyEVQ

class Solution(object):
    def prefixComputation(self, needle):

        n = len(needle)
        pat = [0] * n
        # j is the prefix pointer, and i is the suffix pointer
        j, i = 0, 1

        while i < n:
            if needle[i] == needle[j]:
                pat[i] = j + 1
                i += 1
                j += 1
            elif j == 0: # special case of "j = pat[j - 1]" for j == 0
                pat[i] = 0
                i += 1
            else:
                # don't do i += 1 or pat[i] = pat[j - 1] here.
                # we need to change j:
                #   1) if needle[i] == needle[pat[j - 1]], pat[i] will = pat[j - 1] + 1, not pat[j - 1];
                #   2) if needle[i] != needle[pat[j - 1]], the "pat[i] = pat[j - 1]" will make loop infinite
                #      because i, j don't += 1 anymore.
                j = pat[j - 1]
                # we can't put j = 0 here either , try test case: "aabaaabaaac", "aabaaac".

        #print pat
        return pat

    # return the index of matching point
    def strStr(self, haystack, needle):

        if not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1

        n, m = len(haystack), len(needle)
        i, j = 0, 0
        pat = self.prefixComputation(needle)

        while i < n and j < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            elif j == 0:
                i += 1
            else:
                # it is possible to jump multiple times; it's possible this happens in several
                #   consecutive loops
                j = pat[j - 1]
                # we don't do i += 1 here, because needle[j] don't match haystack[i]
                #   1) needle[:j] matches haystack[i - j:i]
                #   2) after doing the switch on j, j becomes pat[j - 1]
                #   3) so needle[:pat[j - 1]] matches haystack[i - j:i]
                #   4) we still don't know if haystack[i] matches needle[:pat[j - 1] + 1]
                #   5) thus, we needa check haystack[i] and don't do i += 1

        return -1



print Solution().strStr('aabaaabaaac','aabaaac')



'''
# Rude solution with o(mn) time complexity
# In real interview, ask the interviewer if the haystack/needle can be None or "", and corresponding return values

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        if len(haystack) < len(needle):
            return -1
        
        for i, char in enumerate(haystack):
            if char != needle[0]:
                continue
            if haystack[i:i + len(needle)] == needle:
                return i
        
        return -1
'''

