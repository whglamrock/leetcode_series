
from collections import deque

# this kind of question is stupid... but stupid interviewer may ask it

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        i = 0
        ans = []

        while i < len(words):
            # curr stores the words in the current line
            curr = deque()
            # numOfLetters counts the total number of non-empty chars in the current line
            numOfLetters = 0

            # len(curr) == number of slots
            while i < len(words) and numOfLetters + len(curr) + len(words[i]) <= maxWidth:
                curr.append(words[i])
                numOfLetters += len(words[i])
                i += 1

            numOfSpaces = maxWidth - numOfLetters
            line = []

            # assign number of spaces in each slot
            if len(curr) > 1:
                # j is the least number of consecutive spaces
                j = numOfSpaces / (len(curr) - 1)
                extraSpaces = numOfSpaces % (len(curr) - 1)
                while curr:
                    line.append(curr.popleft())
                    if not curr:
                        break
                    line.append(' ' * j)
                    if extraSpaces:
                        line.append(' ')
                        extraSpaces -= 1
            else:
                line.append(curr[0])
                line.append(' ' * numOfSpaces)

            ans.append(''.join(line))

        if ans:
            # if there are consecutive spaces in the string, string.split() will generate empty strings
            lastLine = ans.pop().split(' ')
            wordsInLastLine = deque([item for item in lastLine if item])

            numOfLetters = sum(len(word) for word in wordsInLastLine)
            numOfSpaces = maxWidth - numOfLetters

            line = [' '.join(wordsInLastLine)]
            numOfSpaces -= len(wordsInLastLine) - 1
            line.append(' ' * numOfSpaces)
            ans.append(''.join(line))

        return ans



print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
