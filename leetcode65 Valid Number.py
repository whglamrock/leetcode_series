class Solution:
    def isNumber(self, s: str) -> bool:
        splitter = None
        eCount = 0
        for char in s:
            if char in 'eE':
                eCount += 1
                splitter = char
        if eCount > 1:
            return False
        if eCount == 0:
            return self.isValidSimpleNumber(s)

        left, right = s.split(splitter)
        return self.isValidSimpleNumber(left) and self.isValidSimpleNumber(right) and '.' not in right

    def isValidSimpleNumber(self, s: str) -> bool:
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
