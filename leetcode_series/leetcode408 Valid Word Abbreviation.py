# pay attention to the corner case like ('abbr', 'a02r') in which we should return False

class Solution(object):
    def validWordAbbreviation(self, word, abbr):

        if (not abbr): return False

        i, j = 0, 0
        num = []
        while i < len(word) and j < len(abbr):
            #print i, j
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                if '0' <= abbr[j] <= '9':
                    while j < len(abbr) and '0' <= abbr[j] <= '9':
                        num.append(abbr[j])
                        j += 1
                    if num[0] == '0':
                        return False
                    num = ''.join(num)
                    proceed = int(num)
                    i += proceed
                    num = []
                else:
                    return False

        return i == len(word) and j == len(abbr)



word = "internationalization"
abbr = "i12iz4n"
Sol = Solution()
print Sol.validWordAbbreviation(word, abbr)
