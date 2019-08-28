
# Not actually an easy question because we need to load the string dynamically (lazy load)

class StringIterator(object):
    # we assume the input is always valid
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.compressedStr = compressedString
        self.currIndex = 0
        self.currChar = compressedString[0] if compressedString else ' '
        self.currCount = 0

        # load the first char to get initial state
        self.loadNextChar()

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return ' '

        res = self.currChar
        self.currCount -= 1

        if self.currCount == 0:
            self.loadNextChar()

        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.currCount > 0

    # update the currChar and currCount
    def loadNextChar(self):
        # when we reached the end of the string
        if self.currIndex >= len(self.compressedStr):
            return

        # update the current char
        self.currChar = self.compressedStr[self.currIndex]
        # move to the digit char
        self.currIndex += 1

        # get the count
        countStr = []
        while self.currIndex < len(self.compressedStr) and self.compressedStr[self.currIndex].isdigit():
            countStr.append(self.compressedStr[self.currIndex])
            self.currIndex += 1
        self.currCount = int(''.join(countStr))



# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()