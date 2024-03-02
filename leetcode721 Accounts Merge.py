from collections import defaultdict
from typing import List

# graph + bfs
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToAccountIds = defaultdict(set)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                emailToAccountIds[email].add(i)

        graph = defaultdict(set)
        for email in emailToAccountIds:
            for id1 in emailToAccountIds[email]:
                for id2 in emailToAccountIds[email]:
                    if id1 == id2:
                        continue
                    graph[id1].add(id2)
                    graph[id2].add(id1)

        visited = set()
        ans = []
        for i in range(len(accounts)):
            if i in visited:
                continue
            if i not in graph:
                emails = sorted(set(accounts[i][1:]))
                ans.append([accounts[i][0]] + emails)
                visited.add(i)
            else:
                # bfs
                todo = {i}
                currVisited = set()
                while todo:
                    nextTodo = set()
                    for node in todo:
                        currVisited.add(node)
                        if node not in graph:
                            continue
                        for connectedNode in graph[node]:
                            if connectedNode not in currVisited:
                                currVisited.add(connectedNode)
                                nextTodo.add(connectedNode)
                    todo = nextTodo

                name = accounts[i][0]
                emails = set()
                for accountId in currVisited:
                    for email in accounts[accountId][1:]:
                        emails.add(email)
                ans.append([name] + sorted(emails))
                visited = visited.union(currVisited)

        return ans
