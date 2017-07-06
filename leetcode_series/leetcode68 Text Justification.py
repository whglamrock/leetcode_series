
# note: the lenth of word is guaranteed smaller than maxWidth
# P.S., remember the robin logic operation code:
#   for i in xrange(maxWidth - num_of_letters):
#       cur[i % (len(cur) - 1 or 1)] += ' '

class Solution(object):
    def fullJustify(self, words, maxWidth):

        # the "not words" corner case is also covered in the following
        res = []
        numofletters = 0
        # the len(curr) is the current number of slots needed
        currchunks = []

        for word in words:
            # the currchunk is from the last loop, and len(currchunk) == number of words in this line - 1
            # the condition operator can't be '>='
            if numofletters + len(word) + len(currchunks) > maxWidth:
                for i in xrange(maxWidth - numofletters):
                    # the currchunks has to minus one
                    if len(currchunks) > 1:
                        currchunks[i % (len(currchunks) - 1)] += ' '
                    else:
                        currchunks[0] += ' '
                res.append(''.join(currchunks))
                currchunks = []
                numofletters = 0
            currchunks.append(word)
            numofletters += len(word)

        lastline = ' '.join(currchunks)
        return res + [lastline + ' ' * (maxWidth - len(lastline))]
        #return res + [' '.join(currchunks) + ' ' * (maxWidth - numofletters - len(currchunks) + 1)]
        #return res + [' '.join(curr).ljust(maxWidth)]  # the magical "ljust"



Sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
ans = Sol.fullJustify(words, 16)
for item in ans:
    print item

