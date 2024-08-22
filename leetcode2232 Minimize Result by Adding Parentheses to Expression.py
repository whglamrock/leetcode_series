
# P.S.: test case like '1 * (+1) * 1' isn't allowed
class Solution:
    def minimizeResult(self, expression: str) -> str:
        firstHalf, secondHalf = expression.split('+')[0], expression.split('+')[1]
        indexTo1stLeft, indexTo2ndLeft = {0: 1}, {0: int(firstHalf)}
        for i in range(1, len(firstHalf)):
            firstLeft, secondLeft = int(firstHalf[:i]), int(firstHalf[i:])
            indexTo1stLeft[i] = firstLeft
            indexTo2ndLeft[i] = secondLeft

        indexTo1stRight, indexTo2ndRight = {}, {}
        for i in range(1, len(secondHalf)):
            firstRight, secondRight = int(secondHalf[:i]), int(secondHalf[i:])
            indexTo1stRight[i] = firstRight
            indexTo2ndRight[i] = secondRight
        indexTo1stRight[len(secondHalf)] = int(secondHalf)
        indexTo2ndRight[len(secondHalf)] = 1

        minResult = 2147483647
        ans = ''
        for i in range(len(firstHalf)):
            for j in range(1, len(secondHalf) + 1):
                first, second, third, forth = indexTo1stLeft[i], indexTo2ndLeft[i], indexTo1stRight[j], indexTo2ndRight[j]
                result = first * (second + third) * forth
                if minResult > result:
                    minResult = result
                    ans = firstHalf[:i] + '(' + firstHalf[i:] + '+' + secondHalf[:j] + ')' + secondHalf[j:]

        return ans
