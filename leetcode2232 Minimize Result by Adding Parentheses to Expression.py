
class Solution:
    def minimizeResult(self, expression: str) -> str:
        leftNumStr, rightNumStr = expression.split('+')[0], expression.split('+')[1]
        # P.S. leetcode doesn't allow something like 1 * (+1) * 1 so the 2nd and 3nd number can't be empty
        insertIndexTo1stNum, insertIndexTo2ndNum = {0: 1}, {0: int(leftNumStr)}
        for i in range(1, len(leftNumStr)):
            insertIndexTo1stNum[i] = int(leftNumStr[:i])
            insertIndexTo2ndNum[i] = int(leftNumStr[i:])
        insertIndexTo3rdNum, insertIndexTo4thNum = {len(rightNumStr): int(rightNumStr)}, {len(rightNumStr): 1}
        for i in range(1, len(rightNumStr)):
            insertIndexTo3rdNum[i] = int(rightNumStr[:i])
            insertIndexTo4thNum[i] = int(rightNumStr[i:])

        minResult = 2147483548
        l, r = 0, len(expression)
        for leftIndex in insertIndexTo1stNum:
            firstNum = insertIndexTo1stNum[leftIndex]
            secondNum = insertIndexTo2ndNum[leftIndex]
            for rightIndex in insertIndexTo3rdNum:
                thirdNum = insertIndexTo3rdNum[rightIndex]
                forthNum = insertIndexTo4thNum[rightIndex]
                if firstNum * (secondNum + thirdNum) * forthNum < minResult:
                    minResult = firstNum * (secondNum + thirdNum) * forthNum
                    l, r = leftIndex, rightIndex

        if 0 <= l < len(leftNumStr):
            generatedLeft = leftNumStr[:l] + '(' + leftNumStr[l:]
        else:
            generatedLeft = leftNumStr[:l] + '('

        if 0 <= r < len(rightNumStr):
            generatedRight = rightNumStr[:r] + ')' + rightNumStr[r:]
        else:
            generatedRight = rightNumStr[:r] + ')'

        return generatedLeft + '+' + generatedRight
