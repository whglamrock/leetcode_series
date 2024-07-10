from collections import defaultdict
from typing import List, Dict


# Intuition:
# 1) To achieve O(N) time, we must use DFS.
# 2) Since it's a tree, we never have to worry about cycle. We use a lastNode variable in DFS to avoid going
# backwards -> remember: we never have to worry about visit any node twice since it's a tree structure.
# 3) we need to keep a distanceToBob map for each node so that when we do dfs for Alice we know if she can claim the amount
# 4) First, do dfs for bob to populate the distanceToBob map, and ONLY record the path node in the map if the current node
# has a path to 0
# 5) At last, do dfs for Alice, and the return value for this dfs is the maximum reward from the current node
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        distanceToBob = {}
        self.dfsForBob(bob, -1, 0, graph, distanceToBob)
        return self.dfsForAlice(0, -1, 0, graph, amount, distanceToBob)

    def dfsForAlice(self, currNode: int, lastNode: int, distance: int, graph: Dict[int, set], amount: List[int], distanceToBob: Dict[int, int]) -> int:
        # first check if we can claim the income
        if currNode in distanceToBob:
            if distanceToBob[currNode] < distance:
                incomeForCurrNode = 0
            elif distanceToBob[currNode] == distance:
                incomeForCurrNode = amount[currNode] // 2
            else:
                incomeForCurrNode = amount[currNode]
        else:
            incomeForCurrNode = amount[currNode]

        # leaf node
        if len(graph[currNode]) == 1 and list(graph[currNode])[0] == lastNode:
            return incomeForCurrNode

        # P.S., cannot set it to 0
        extraIncomeInChildren = -2147483648
        for connectedNode in graph[currNode]:
            if connectedNode == lastNode:
                continue
            extraIncomeInChildren = max(extraIncomeInChildren, self.dfsForAlice(connectedNode, currNode, distance + 1, graph, amount, distanceToBob))

        return incomeForCurrNode + extraIncomeInChildren

    def dfsForBob(self, currNode: int, lastNode: int, distance: int, graph: Dict[int, set], distanceToBob: Dict[int, int]) -> bool:
        if currNode not in graph:
            return False
        if currNode == 0:
            distanceToBob[0] = distance
            return True

        foundPathTo0 = False
        for connectedNode in graph[currNode]:
            if connectedNode == lastNode:
                continue
            if self.dfsForBob(connectedNode, currNode, distance + 1, graph, distanceToBob):
                foundPathTo0 = True
                break

        if foundPathTo0:
            # only add the currentNode to map if there is a path to 0
            distanceToBob[currNode] = distance
            return True
        return False
