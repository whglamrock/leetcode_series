from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numOfProvinces = 0
        n = len(isConnected)
        for i in range(n):
            if isConnected[i][i] == 0:
                continue
            self.bfs(isConnected, i)
            numOfProvinces += 1

        return numOfProvinces

    def bfs(self, isConnected: List[List[int]], city: int):
        n = len(isConnected)
        todo = {city}
        while todo:
            nextTodo = set()
            for node in todo:
                # means this node is visited
                isConnected[node][node] = 0
                for nextNode, value in enumerate(isConnected[node]):
                    if value == 0 or node == nextNode:
                        continue
                    # cut the connection
                    isConnected[node][nextNode] = 0
                    isConnected[nextNode][node] = 0
                    nextTodo.add(nextNode)
            todo = nextTodo


print(Solution().findCircleNum([
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]))
