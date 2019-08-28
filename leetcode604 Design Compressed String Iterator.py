
# Not actually an easy question because we need to load the string dynamically (lazy load)

class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.compressedStr = compressedString

        self.currChar = compressedString[0] if compressedString else ' '
        self.currIndex = 0
        self.currCount = 0

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
        if self.currIndex >= len(self.compressedStr):
            return
        self.currChar = self.compressedStr[self.currIndex]

        # move the index to digit char
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