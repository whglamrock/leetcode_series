from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.dfs(k, n, [], 0)
        return self.ans

    def dfs(self, k: int, n: int, path: List[int], currSum: int):
        if k == 0:
            if currSum == n:
                self.ans.append(path)
            return

        if path and currSum + path[-1] + 1 > n:
            return

        if path:
            for nextNum in range(path[-1] + 1, 10):
                self.dfs(k - 1, n, path + [nextNum], currSum + nextNum)
        else:
            for nextNum in range(1, 10):
                self.dfs(k - 1, n, [nextNum], nextNum)
