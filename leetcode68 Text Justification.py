
# note: the lenth of word is guaranteed smaller than maxWidth
# P.S., remember the robin logic operation code:
#   for i in xrange(maxWidth - numofletters):
#       currline[i % (len(currline) - 1 or 1)] += ' '

class Solution(object):
    def fullJustify(self, words, maxWidth):

        # the "not words" corner case is also covered in the following
        res = []
        numofletters = 0
        # the len(currline) is the current number of slots needed
        currline = []

        for word in words:
            # the currline is from the last loop, and len(currline) == number of words in this line - 1
            # the condition operator can't be '>='
            if numofletters + len(word) + len(currline) > maxWidth:
                for i in xrange(maxWidth - numofletters):
                    # the currline has to minus one
                    if len(currline) > 1:
                        currline[i % (len(currline) - 1)] += ' '
                    else:
                        currline[0] += ' '
                res.append(''.join(currline))
                currline = []
                numofletters = 0
            currline.append(word)
            numofletters += len(word)

        lastline = ' '.join(currline)
        return res + [lastline + ' ' * (maxWidth - len(lastline))]
        #return res + [' '.join(currline) + ' ' * (maxWidth - numofletters - len(currline) + 1)]
        #return res + [' '.join(currline).ljust(maxWidth)]  # the magical "ljust"



Sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
ans = Sol.fullJustify(words, 15)
for item in ans:
    print item

