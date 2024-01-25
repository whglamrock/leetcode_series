from collections import defaultdict
from typing import Dict, List

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        nodeToChildren = defaultdict(set)
        for i, parent in enumerate(parents):
            if i == 0:
                continue
            nodeToChildren[parent].add(i)

        nodeToNumOfNodes = {}
        self.traverseTree(nodeToChildren, nodeToNumOfNodes, 0)

        highestScore = 0
        scoreToNumOfNodes = defaultdict(int)
        for node in range(len(parents)):
            subtreeSizes = []
            if node in nodeToChildren:
                for child in nodeToChildren[node]:
                    subtreeSizes.append(nodeToNumOfNodes[child])
            if parents[node] != -1:
                subtreeSizes.append(nodeToNumOfNodes[0] - nodeToNumOfNodes[node])

            score = 1 if subtreeSizes else 0
            for i in range(len(subtreeSizes)):
                score *= subtreeSizes[i]
            scoreToNumOfNodes[score] += 1
            highestScore = max(highestScore, score)

        return scoreToNumOfNodes[highestScore]

    def traverseTree(self, nodeToChildren: Dict[int, set], nodeToNumOfNodes: Dict[int, int], node: int):
        if node not in nodeToChildren:
            nodeToNumOfNodes[node] = 1
            return 1

        numOfNodes = 1
        for child in nodeToChildren[node]:
            numOfNodes += self.traverseTree(nodeToChildren, nodeToNumOfNodes, child)
        nodeToNumOfNodes[node] = numOfNodes
        return numOfNodes
