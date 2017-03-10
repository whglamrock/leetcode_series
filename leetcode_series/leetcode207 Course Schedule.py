# Another BFS way from: https://discuss.leetcode.com/topic/13854/easy-bfs-topological-sort-java/7
# running time O(V+E). V: number of vertexes, E: number of edges

# the following is classical topo-sort solution

import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        if not prerequisites or numCourses == 0:
            return True

        greater = collections.defaultdict(set)
        less = collections.defaultdict(set)

        for edge in prerequisites:
            s, e = edge
            greater[s].add(e)
            less[e].add(s)

        queue = collections.deque()
        for i in xrange(numCourses):
            if i not in greater:
                queue.append(i)

        while queue:
            i = queue.popleft()
            if i in less:
                for j in less[i]:
                    greater[j].discard(i)
                    if len(greater[j]) == 0:
                        queue.append(j)
                        del greater[j]

        return len(greater) == 0


Sol = Solution()
numCourses = 2
prerequisites = [[1,0]]
print Sol.canFinish(numCourses, prerequisites)


'''
# my original O(V^2) solution got TLE. But in practical interview, it should be accepted.
class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        dick = {}
        for course in prerequisites:
            [a, b] = course
            if b in dick:
                dick[b].add(a)
            else:
                dick[b] = {a}
            todo = set()
            todo.add(a)
            while todo:
                next = set()
                for node in todo:
                    if node in dick:
                        if b in dick[node]:
                            return False
                        next |= dick[node]
                todo = next

        return True
'''



