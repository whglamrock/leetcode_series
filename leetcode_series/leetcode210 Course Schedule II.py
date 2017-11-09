
# topological sort solution
# idea from lc207

import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):

        if numCourses == 0: return []
        if not prerequisites or len(prerequisites) == 0:
            return [i for i in xrange(numCourses)]

        less = collections.defaultdict(set)
        greater = collections.defaultdict(set)

        for item in prerequisites:
            less[item[1]].add(item[0])
            greater[item[0]].add(item[1])

        queue = collections.deque()
        for i in xrange(numCourses):
            if i not in greater:
                queue.append(i)

        order = []
        while queue:
            i = queue.popleft()
            if i in less:
                for j in less[i]:
                    greater[j].discard(i)
                    if len(greater[j]) == 0:
                        del greater[j]
                        queue.append(j)
            order.append(i)

        if len(greater) > 0:
            return []
        else:
            return order



Sol = Solution()
numCourses = 2
prerequisites = [[1,0]]
print Sol.findOrder(numCourses, prerequisites)
