from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def addOperators(self, num: str, target: int) -> List[str]:
        self.ans = []
        for i in range(1, len(num) + 1):
            if i == 1 or num[0] != '0':
                numStr = num[i:]
                currExpression = num[:i]
                currResult = int(currExpression)
                lastNum = int(currExpression)
                self.dfs(numStr, target, currExpression, currResult, lastNum)

        return self.ans

    def dfs(self, numStr: str, target: int, currExpression: str, currResult: int, lastNum: int):
        if not numStr:
            if currResult == target:
                self.ans.append(currExpression)
            return

        for i in range(1, len(numStr) + 1):
            # we just need to make sure the currentNum doesn't start with 0
            # the nextNumStr will be handled in next recursion
            currNumStr = numStr[:i]
            nextNumStr = numStr[i:]
            if i == 1 or numStr[0] != '0':
                self.dfs(nextNumStr, target, currExpression + '+' + currNumStr, currResult + int(currNumStr), int(currNumStr))
                self.dfs(nextNumStr, target, currExpression + '-' + currNumStr, currResult - int(currNumStr), -int(currNumStr))
                self.dfs(nextNumStr, target, currExpression + '*' + currNumStr, currResult - lastNum + int(currNumStr) * lastNum, int(currNumStr) * lastNum)


print(Solution().addOperators('105', 5))
print(Solution().addOperators('00', 0))
print(Solution().addOperators('232', 8))
print(Solution().addOperators('123', 6))
print(Solution().addOperators('3456237490', 9191))
