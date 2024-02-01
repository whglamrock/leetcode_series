from collections import defaultdict
from typing import List

# Guaranteed O(N ^ 2) DP solution
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        indexToPossibleJumps = defaultdict(set)
        indexToPossibleJumps[0].add(1)

        for i in range(1, n):
            for j in range(i):
                distance = stones[i] - stones[j]
                if distance in indexToPossibleJumps[j]:
                    indexToPossibleJumps[i].add(distance)
                    indexToPossibleJumps[i].add(distance - 1)
                    indexToPossibleJumps[i].add(distance + 1)
        return n - 1 in indexToPossibleJumps


print(Solution().canCross([0, 1, 2, 4, 5, 6, 7, 9, 10, 11, 13]))
print(Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11]))


'''
# dfs + memoization
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        self.stones = stones
        self.stoneToIndex = {}
        for i, stone in enumerate(stones):
            self.stoneToIndex[stone] = i
        
        return self.dfs(1, 1)
    
    @lru_cache(None)
    def dfs(self, prevJump: int, i: int) -> bool:
        #print(prevJump, i)
        if i == len(self.stones) - 1:
            return True

        stone = self.stones[i]
        canReachLastStone = False
        for jump in range(max(prevJump - 1, 1), prevJump + 2):
            if stone + jump in self.stoneToIndex:
                nextIndex = self.stoneToIndex[stone + jump]
                canReachLastStone |= self.dfs(jump, nextIndex)
        
        return canReachLastStone
'''