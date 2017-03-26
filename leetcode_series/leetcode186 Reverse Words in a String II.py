
# pay attention to the reverser() function. It uses extra space.
# O(1) space, O(N) time

class Solution(object):
    def reverseWords(self, s):

        i, j = 0, len(s)-1
        while i < j:    # python reverse() function use extra space with iterator.
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        i = 0
        while i < len(s):
            j = i
            while i < len(s) and s[i] != ' ':    # "i < len(s)" is important!
                i += 1
            mark = i
            i -= 1
            while j < len(s) and i >= 0 and j <= i:    # "j < len(s) and i >= 0" is important!
                s[i], s[j] = s[j], s[i]
                j += 1
                i -= 1
            i = mark + 1