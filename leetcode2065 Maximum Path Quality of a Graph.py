from collections import defaultdict
from copy import deepcopy
from typing import List

# remember the trick of caching nodeToVisitedTimeAndQuality. We don't necessarily need to save the min visited time
# and max quality: we just need to save the previously visited time and quality and filter out the invalid case so
# that there won't be any combination of (bigger time and smaller quality) cases we bfs later.
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(set)
        edgeToTime = {}
        for i, j, time in edges:
            graph[i].add(j)
            graph[j].add(i)
            edgeToTime[(i, j)] = time
            edgeToTime[(j, i)] = time

        nodeToMaxQuality = {}
        nodeToVisitedTimeAndQuality = {0: [0, values[0]]}
        todo = [[0, values[0], 0, {0}]]
        while todo:
            nextTodo = []
            for node, currQuality, currTime, visitedNodes in todo:
                if node not in nodeToMaxQuality or nodeToMaxQuality[node] < currQuality:
                    nodeToMaxQuality[node] = currQuality
                for nextNode in graph[node]:
                    nextTime = currTime + edgeToTime[(node, nextNode)]
                    if nextTime > maxTime:
                        continue
                    nextQuality = currQuality + values[nextNode] if nextNode not in visitedNodes else currQuality
                    if nextNode in nodeToVisitedTimeAndQuality:
                        prevTime, prevQuality = nodeToVisitedTimeAndQuality[nextNode]
                        if nextTime >= prevTime and nextQuality < prevQuality:
                            continue
                    nodeToVisitedTimeAndQuality[nextNode] = [nextTime, nextQuality]
                    nextVisitedNodes = deepcopy(visitedNodes)
                    nextVisitedNodes.add(nextNode)
                    nextTodo.append([nextNode, nextQuality, nextTime, nextVisitedNodes])
                    if nextNode not in nodeToMaxQuality:
                        nodeToMaxQuality[nextNode] = nextQuality
                    else:
                        nodeToMaxQuality[nextNode] = max(nextQuality, nodeToMaxQuality[nextNode])
            todo = nextTodo

        return nodeToMaxQuality[0]
