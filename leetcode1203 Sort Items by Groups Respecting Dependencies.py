
from collections import defaultdict, deque

# 2 level topology sort solution idea: https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/discuss/402401/Python-Use-topologically-sorted-items-and-groups-to-get-the-desired-order.
# This questions requires a little modification to the template topo-sort solution:
    # in indegree, if a node is greater than nobody, indegree[node] == 0

class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """

        # use a new group number for each isolated node
        for i in xrange(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        groupGraph, itemGraph = {x: set() for x in xrange(m)}, {y: set() for y in xrange(n)}
        indegreeGroup, indegreeItem = defaultdict(int), defaultdict(int)

        for i in xrange(n):
            if not beforeItems[i]:
                continue
            groupI = group[i]
            for j in beforeItems[i]:
                groupJ = group[j]
                # build single item's graph & indegree first
                itemGraph[j].add(i)
                indegreeItem[i] += 1
                # do remember to check "groupI != groupJ"!
                # the solution not deduping seems to also work we dedupe logically makes more sense
                if groupI != groupJ and groupI not in groupGraph[groupJ]:
                    groupGraph[groupJ].add(groupI)
                    indegreeGroup[groupI] += 1

        topoSortedItems = self.topoSort(itemGraph, indegreeItem)
        topoSortedGroups = self.topoSort(groupGraph, indegreeGroup)
        if not topoSortedItems or not topoSortedGroups:
            return []

        orderedItemWithinGroup = defaultdict(list)
        for item in topoSortedItems:
            orderedItemWithinGroup[group[item]].append(item)

        ans = []
        for groupI in topoSortedGroups:
            ans += orderedItemWithinGroup[groupI]
        return ans

    def topoSort(self, graph, indegree):
        topoOrder = []
        q = deque([node for node in graph if indegree[node] == 0])

        while q:
            i = q.popleft()
            topoOrder.append(i)
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

        return topoOrder if len(topoOrder) == len(graph) else []



