from collections import defaultdict
from typing import List

# Tweaked O(N) time BFS solution. The naive O(N ^ 2) graph solution gets MLE in the stupid leetcode.
# To deal with annoying edge cases like [7, 7, 7, ..., 7], we need to use a visitedVals set to store the visited node values.
# Note the trick of checking the visitedVal before bulk adding all nodes with the same value to the nextTodo.
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        numToIndexes = defaultdict(list)
        for i, num in enumerate(arr):
            numToIndexes[num].append(i)

        todo = {0}
        visited = set()
        visitedVals = set()
        steps = 0
        while todo:
            nextTodo = set()
            for node in todo:
                if node == n - 1:
                    return steps

                visited.add(node)
                for connectedNode in [node - 1, node + 1]:
                    if 0 <= connectedNode < n and connectedNode not in visited:
                        nextTodo.add(connectedNode)

                if arr[node] in visitedVals:
                    continue
                for connectedNode in numToIndexes[arr[node]]:
                    if connectedNode not in visited:
                        nextTodo.add(connectedNode)
                visitedVals.add(arr[node])

            todo = nextTodo
            steps += 1

        return steps
