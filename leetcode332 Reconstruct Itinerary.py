from collections import defaultdict
from copy import deepcopy
from heapq import *
from typing import List


# 1) Optimal solution is using Euler Path algorithm (see code at the bottom) but it's not a must in real interview.
# Euler Path search algorithm: http://stackoverflow.com/questions/17467228/looking-for-algorithm-finding-euler-path
# 2) A naive priorityQueue + bfs solution should suffice in real interview.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        srcToDestToCount = defaultdict(dict)
        for src, dest in tickets:
            if dest not in srcToDestToCount[src]:
                srcToDestToCount[src][dest] = 1
            else:
                srcToDestToCount[src][dest] += 1

        pq = [[['JFK'], srcToDestToCount]]
        while pq:
            currPath, availableSrcToDestToCount = heappop(pq)
            if len(currPath) == len(tickets) + 1:
                return currPath
            src = currPath[-1]
            if src not in availableSrcToDestToCount:
                continue
            for dest in availableSrcToDestToCount[src]:
                nextPath = deepcopy(currPath)
                nextPath.append(dest)
                nextSrcToDestToCount = deepcopy(availableSrcToDestToCount)
                nextSrcToDestToCount[src][dest] -= 1
                if not nextSrcToDestToCount[src][dest]:
                    del nextSrcToDestToCount[src][dest]
                heappush(pq, [nextPath, nextSrcToDestToCount])

        return []


print(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))


'''
# optimal Euler path theory. It's not a must in real interview.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        srcToDests = defaultdict(list)
        for src, dest in tickets:
            srcToDests[src].append(dest)
        
        stack = ['JFK']
        ans = []
        while stack:
            while stack[-1] in srcToDests and srcToDests[stack[-1]]:
                stack.append(srcToDests[stack[-1]].pop())
            ans.append(stack.pop())
        
        return ans[::-1]
'''
