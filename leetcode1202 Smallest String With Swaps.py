from collections import Counter, defaultdict
from typing import List


# Time complexity is max(O(nlog(avg(size of the group))), O(numOfPairs)), where n = len(s).
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(set)
        for node, connectedNode in pairs:
            graph[node].add(connectedNode)
            graph[connectedNode].add(node)

        indexToGroup = {}
        currGroup = 0
        n = len(s)
        groupToIndexes = defaultdict(set)

        for i in range(n):
            if i in indexToGroup:
                continue
            # i is not in pairs
            if i not in graph:
                indexToGroup[i] = currGroup
                groupToIndexes[currGroup] = {i}
                currGroup += 1
                continue

            todo = {i}
            while todo:
                nextTodo = set()
                for node in todo:
                    indexToGroup[node] = currGroup
                    groupToIndexes[currGroup].add(node)
                    for connectedNode in graph[node]:
                        if connectedNode in indexToGroup:
                            continue
                        indexToGroup[connectedNode] = currGroup
                        nextTodo.add(connectedNode)
                todo = nextTodo
            currGroup += 1

        ans = [''] * n
        for i in range(n):
            if ans[i]:
                continue

            group = indexToGroup[i]
            chars = [s[index] for index in groupToIndexes[group]]
            charCount = Counter(chars)
            sortedChars = []
            for char in sorted(charCount.keys()):
                sortedChars.append(char * charCount[char])
            sortedCharStr = ''.join(sortedChars)

            j = 0
            for index in sorted(groupToIndexes[group]):
                ans[index] = sortedCharStr[j]
                j += 1

        return ''.join(ans)
