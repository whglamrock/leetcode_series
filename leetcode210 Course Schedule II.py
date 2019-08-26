
from collections import defaultdict, deque

# topological sort solution
# idea from lc207

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        less, greater = self.buildRelationship(prerequisites)

        q = deque()
        for i in xrange(numCourses):
            if i not in greater:
                q.append(i)

        ans = []
        while q:
            j = q.popleft()
            ans.append(j)
            # this means no course depends on j
            if j not in less:
                continue
            for i in less[j]:
                greater[i].discard(j)
                if not greater[i]:
                    del greater[i]
                    q.append(i)

        return ans if not greater else []

    def buildRelationship(self, prerequisites):
        less, greater = defaultdict(set), defaultdict(set)
        # j is i's prerequisite
        for i, j in prerequisites:
            less[j].add(i)
            greater[i].add(j)

        return less, greater



print Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
