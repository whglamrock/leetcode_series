
from collections import defaultdict, deque

# let's see some bullshit edge cases leetcode gives:
    # 1. [1], [[1],[1],[1]]
    # 2. [1], [[],[]]
    # 3. [1], []
    # 4. [1], [[1],[2,3],[3,2]]

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not seqs:
            return not org

        less, greater = self.buildRelationship(seqs)

        # using a numSet to gather all numbers occurred in seqs
        numSet = set()
        for seq in seqs:
            for num in seq:
                numSet.add(num)
        # the topology queue is based on numSet and ans constructed from it will be used to compare with org
        q = deque()
        for num in numSet:
            if num not in greater:
                q.append(num)

        ans = []
        while q:
            if len(q) != 1:
                return False
            i = q.popleft()
            ans.append(i)
            if i in less:
                for j in less[i]:
                    greater[j].discard(i)
                    if not greater[j]:
                        del greater[j]
                        q.append(j)

        return ans == org and not greater

    def buildRelationship(self, seqs):
        less, greater = defaultdict(set), defaultdict(set)
        # i is lower than j
        for seq in seqs:
            for i in xrange(len(seq) - 1):
                less[seq[i]].add(seq[i + 1])
                greater[seq[i + 1]].add(seq[i])
        return less, greater



print Solution().sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3]])
print Solution().sequenceReconstruction([4, 1, 5, 2, 6, 3], [[5, 2, 6, 3], [4, 1, 5, 2]])
