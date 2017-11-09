
# same(or simialr) time/space complexity, but more beautiful code

class Solution(object):
    def wordPattern(self, pattern, str):

        x = str.split(' ')
        lsp = len(set(pattern))
        lsx = len(set(x))
        return len(x)==len(pattern) and lsx==lsp and lsp== len(set(zip(pattern, x)))



Sol = Solution()
print Sol.wordPattern('abba', 'dog dig dig dog')



'''
# my original code (stupid version):

class Solution(object):
    def wordPattern(self, pattern, str):

        dick = {}
        strdick = {}
        for i in xrange(len(pattern)):
            if pattern[i] not in dick:
                dick[pattern[i]] = [i]
            else:
                dick[pattern[i]].append(i)

        string = str.split(' ')
        if len(string) != len(pattern):
            return False

        for j in xrange(len(string)):
            if string[j] not in strdick:
                strdick[string[j]] = [j]
            else:
                strdick[string[j]].append(j)

        for item in dick.values():
            if item not in strdick.values():
                return False

        return True
'''

