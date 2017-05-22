
# KMP algorithm.
# Theory from youtube: https://www.youtube.com/watch?v=GTJr8OvyEVQ

class Solution(object):
    def ComputePrefixFunction(self, needle):

        pat = [0] * len(needle)
        # j is the prefix pointer, i is the suffix pointer
        j, i = 0, 1

        while i < len(needle):
            if needle[i] == needle[j]:
                pat[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                pat[i] = 0
                i += 1
            else:
                j = pat[j - 1]

        return pat

    def strStr(self, haystack, needle):

        if (not needle) or len(needle) == 0:
            return 0
        if (not haystack) or len(haystack) < len(needle):
            return -1

        n = len(haystack)
        m = len(needle)
        # at this time, i is the haystack pointer, j is the needle pointer
        i, j = 0, 0
        pat = self.ComputePrefixFunction(needle)

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            elif j == 0:
                i += 1
            else:
                j = pat[j - 1]

        return -1



Sol = Solution()
print Sol.strStr('abcdefgsjabcde','bcde')



'''
# Rude solution with o(mn) time complexity
# In real interview, ask the interviewer if the haystack/needle can be None or "", and corresponding
# return values
class Solution(object):
    def strStr(self, haystack, needle):

        if (not needle):
            return 0

        if (not haystack):
            return -1

        if len(haystack) < len(needle):
            return -1

        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                j = 1
                while i + j < len(haystack) and j < len(needle):
                    if haystack[i + j] != needle[j]:
                        break
                    j += 1
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    break
            i += 1

        return -1
'''

