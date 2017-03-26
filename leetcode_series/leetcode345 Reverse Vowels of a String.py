
# set two pointers from head and back, respectively.

class Solution(object):
    def reverseVowels(self, s):

        if not s:
            return s
        s = list(s)   # remember this operator
        n = len(s)
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        i, j = 0, n-1
        while i<j:
            if s[i] in vowel and s[j] in vowel:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] in vowel:
                j -= 1
            elif s[j] in vowel:
                i += 1
            else:
                i += 1
                j -= 1

        return ''.join(s)   # remember this operator