
# interesting question
# idea from Stefen: https://discuss.leetcode.com/topic/24176/1-7-lines-python-length-prefixes

class Codec:

    def encode(self, strs):

        return ''.join(str(len(s)) + ':' + s for s in strs)

    def decode(self, s):

        strs = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != ':':
                j += 1
            length = int(s[i: j])
            strs.append(s[j + 1: j + length + 1])
            i = j + length + 1

        return strs



Sol = Codec()
strings = ['a', 'saf', '12:4rf', '@$%']
s = Sol.encode(strings)
print s
print Sol.decode(s)
