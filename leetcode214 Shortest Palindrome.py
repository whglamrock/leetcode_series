
# the question is actually find the longests palindrome prefix

class Solution(object):
    def shortestPalindrome(self, s):

        # to calculate the 'pattern' of 'haystack'.
        def ComputePrefixFunction(needle):

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

        news = s + '#' + s[::-1]
        # the trick is to use KMP table to find the longest matching prefix of news
        KMPtable = ComputePrefixFunction(news)
        compensate = s[:KMPtable[-1] - 1:-1]

        return compensate + s