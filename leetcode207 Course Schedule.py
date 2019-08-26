
from collections import deque, defaultdict

# the following is classical topo-sort solution which takes O(V + E), where V: number of vertexes,
    # E: number of edges

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites or numCourses == 0:
            return True

        less, greater = self.buildRelationship(prerequisites)
        q = deque()
        for i in xrange(numCourses):
            if i not in greater:
                q.append(i)

        while q:
            j = q.popleft()
            if j not in less:
                continue
            for i in less[j]:
                greater[i].discard(j)
                if not greater[i]:
                    del greater[i]
                    q.append(i)

        return not greater

    # build less, greater lists so we can conduct the topology sort algorithm
    def buildRelationship(self, prerequisites):
        less, greater = defaultdict(set), defaultdict(set)
        # j is i's prerequisite
        for i, j in prerequisites:
            less[j].add(i)
            greater[i].add(j)
        return less, greater



print Solution().canFinish(2, [[1,0],[0,1]])
print Solution().canFinish(4, [[1,0],[2,1],[3,1],[3,0],[3,2]])



