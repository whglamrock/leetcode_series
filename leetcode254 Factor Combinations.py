from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def getFactors(self, n: int) -> List[List[int]]:
        self.ans = []
        self.dfs([n], 2)
        return self.ans

    def dfs(self, curr: List[int], i: int):
        num = curr.pop()
        while i * i <= num:
            div = num // i
            if num % i == 0:
                self.ans.append(curr + [i, div])
                self.dfs(curr + [i, div], i)

            i += 1
