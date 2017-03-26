
# note: the lenth of word is guaranteed smaller than maxWidth

class Solution(object):
    def fullJustify(self, words, maxWidth):

        if not words or not maxWidth:
            return ['']

        stack = []
        curr = []
        currlen = 0
        for i, word in enumerate(words):
            # if adding current word exceeds the maxWidth
            if len(word) + currlen > maxWidth:
                stack.append(curr)
                curr, currlen = [], 0
            curr.append(word)
            currlen += len(word)

            # if adding current word reaches the maxWidth
            if currlen == maxWidth:
                stack.append(curr)
                curr, currlen = [], 0
            # we can at least insert a space and look at the next word
            else:
                currlen += 1

        # deal with last line
        if curr:
            stack.append(curr)

        ans = []
        for group in stack[:len(stack) - 1]:

            lensum = sum(len(word) for word in group)
            numofwords = len(group)
            if numofwords > 1:
                lenofintervals = (maxWidth - lensum) / (numofwords - 1)
            else:
                lenofintervals = 0
            if numofwords > 1:
                # leftover is the remainder
                leftover = (maxWidth - lensum) % (numofwords - 1)
            else:
                leftover = 0
            intervals = []

            for i in xrange(numofwords - 1):
                # length is the customized length of this interval
                length = lenofintervals
                if leftover:
                    length += 1
                    leftover -= 1
                intervals.append(length)
            intervals.append(0)

            string = ''
            for i, word in enumerate(group):
                string += word
                for j in xrange(intervals[i]):
                    string += ' '
            # when there is only one word in this line
            if len(string) < maxWidth:
                for j in xrange(maxWidth - len(string)):
                    string += ' '
            ans.append(string)

        # here we deal with the last one
        string = ''
        for i, word in enumerate(stack[-1]):
            string += word
            if i != len(stack[-1]) - 1:
                string += ' '

        if len(string) < maxWidth:
            for j in xrange(maxWidth - len(string)):
                string += ' '
        ans.append(string)

        return ans