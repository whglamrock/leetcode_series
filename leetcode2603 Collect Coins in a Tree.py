from collections import defaultdict
from typing import List

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        tree = defaultdict(set)
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        nonCoinLeafNodes = set()
        coinNodes = set()
        for i, coin in enumerate(coins):
            if coin == 1:
                coinNodes.add(i)

        for node in tree:
            if len(tree[node]) == 1 and node not in coinNodes:
                nonCoinLeafNodes.add(node)

        # bfs to trim non-leaf nodes:
        todo = nonCoinLeafNodes
        while todo:
            nextTodo = set()
            for node in todo:
                if node not in tree:
                    continue
                # all leaf node only has one connectedNode
                connectedNode = list(tree[node])[0]
                del tree[node]
                tree[connectedNode].discard(node)
                # in this case, the connectedNode is the last node left in the tree.
                # it will be trimmed no matter it has a coin or not
                if len(tree[connectedNode]) == 0:
                    del tree[connectedNode]
                    continue
                if len(tree[connectedNode]) == 1 and connectedNode not in coinNodes:
                    nextTodo.add(connectedNode)
            todo = nextTodo

        # bfs to trim coin leaf nodes 2 rounds
        coinLeafNodes = set()
        for node in coinNodes:
            if len(tree[node]) == 1:
                coinLeafNodes.add(node)
        # 1st round
        nextRound = set()
        for node in coinLeafNodes:
            if node not in tree:
                continue
            connectedNode = list(tree[node])[0]
            del tree[node]
            tree[connectedNode].discard(node)
            if len(tree[connectedNode]) == 0:
                del tree[connectedNode]
                continue
            if len(tree[connectedNode]) == 1:
                nextRound.add(connectedNode)
        # 2nd round
        for node in nextRound:
            if node not in tree:
                continue
            connectedNode = list(tree[node])[0]
            tree[connectedNode].discard(node)
            if len(tree[connectedNode]) == 0:
                del tree[connectedNode]
            del tree[node]

        # 1. if we have m nodes, we for sure have m - 1 edges (in a tree structure)
        # total number of steps will always be 2 * number of edges no matter where you start
        # 2. have to consider after trimming there is 0 node left
        return max(2 * (len(tree) - 1), 0)


print(Solution().collectTheCoins(coins=[1, 0, 0, 0, 0, 1], edges=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]))
print(Solution().collectTheCoins(coins=[0, 0, 0, 1, 1, 0, 0, 1], edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7]]))
print(Solution().collectTheCoins(coins=[0, 0], edges=[[0, 1]]))
