
class Solution(object):
    def __init__(self):
        self.ans = 0

    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        self.recursion(text)
        return self.ans

    def recursion(self, text):
        i, j = 0, len(text) - 1
        # considering when text's length is odd/even
        # if we can ever find a prefix & suffix match, i will < j after the while loop
        while i < j and text[:i + 1] != text[j:]:
            i += 1
            j -= 1

        # not using i + 1 < j here; considering test case like 'abab'
        if i < j:
            self.ans += 2
            if i + 1 < j:
                self.recursion(text[i + 1: j])
        else:
            self.ans += 1



print Solution().longestDecomposition('antaprezatepzapreanta')
print Solution().longestDecomposition('ghiabcdefhelloadamhelloabcdefghi')
print Solution().longestDecomposition('evlotevlot')