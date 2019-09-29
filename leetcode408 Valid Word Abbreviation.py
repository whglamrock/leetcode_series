
# pay attention to the corner case like ('abbr', 'a02r') in which we should return False

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if not word:
            return not abbr

        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue

            # abbr[j] == '0' is a really stupid test case
            if not abbr[j].isdigit() or abbr[j] == '0':
                return False

            num = []
            while j < len(abbr) and abbr[j].isdigit():
                num.append(abbr[j])
                j += 1
            num = int(''.join(num))
            i += num

        return i == len(word) and j == len(abbr)



print Solution().validWordAbbreviation("internationalization", "i12iz4n")
