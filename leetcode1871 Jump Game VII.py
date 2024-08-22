
# O(N) BFS solution. Intuition: https://leetcode.com/problems/jump-game-vii/solutions/1236272/java-bfs-detailed-analysis-o-n-bfs-solution/
# The key here is to use a maxReach to track the index we have reached to narrow down the search range. Another important
# note is that each nextTodo list is sorted in nature.
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False

        todo = [0]
        maxReach = 0
        while todo:
            nextTodo = []
            for i in todo:
                if i == len(s) - 1:
                    return True
                for j in range(max(maxReach, i + minJump), min(len(s), i + maxJump + 1)):
                    if s[j] == '0':
                        nextTodo.append(j)

                maxReach = max(maxReach, i + maxJump + 1)

            todo = nextTodo

        return False
