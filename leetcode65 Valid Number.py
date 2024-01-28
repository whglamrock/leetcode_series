class Solution:
    def isNumber(self, s: str) -> bool:
        eCount = 0
        digitCount = 0
        splitter = ''
        for char in s:
            if char in 'eE':
                eCount += 1
                splitter = char
            if char.isdigit():
                digitCount += 1
        if eCount > 1 or digitCount == 0:
            return False
        if eCount == 0:
            return self.isValidNumber(s)

        leftNum, rightNum = s.split(splitter)[0], s.split(splitter)[1]
        return self.isValidNumber(leftNum) and '.' not in rightNum and self.isValidNumber(rightNum)

    def isValidNumber(self, s: str) -> bool:
        if not s:
            return False
        if s[0] in '+-':
            s = s[1:]

        dotCount = 0
        digitCount = 0
        for char in s:
            if char == '.':
                dotCount += 1
            elif char.isdigit():
                digitCount += 1
            else:
                return False

        return dotCount <= 1 and digitCount > 0
