from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.dfs(0, [], 0, candidates, target)
        return self.ans

    def dfs(self, index: int, curr: List[int], currSum: int, candidates: List[int], target: int):
        if currSum > target:
            return
        if currSum == target:
            self.ans.append(curr)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(i + 1, curr + [candidates[i]], currSum + candidates[i], candidates, target)
