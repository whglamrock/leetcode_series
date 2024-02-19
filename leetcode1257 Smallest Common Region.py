from typing import List

# using the include relationship build a tree, then find the lowest common ancestor of 2 nodes.
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        nodeToParent = {}
        for regionList in regions:
            biggerRegion = regionList[0]
            for i in range(1, len(regionList)):
                nodeToParent[regionList[i]] = biggerRegion

        depth1 = 0
        curr = region1
        while curr in nodeToParent:
            curr = nodeToParent[curr]
            depth1 += 1
        depth2 = 0
        curr = region2
        while curr in nodeToParent:
            curr = nodeToParent[curr]
            depth2 += 1

        if depth1 < depth2:
            for i in range(depth2 - depth1):
                region2 = nodeToParent[region2]
        elif depth1 > depth2:
            for i in range(depth1 - depth2):
                region1 = nodeToParent[region1]

        todo = {region1, region2}
        while len(todo) > 1:
            nextTodo = set()
            for region in todo:
                nextTodo.add(nodeToParent[region])
            todo = nextTodo

        return list(todo)[0]
