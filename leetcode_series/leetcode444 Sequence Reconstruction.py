
import collections

class Solution(object):
    def sequenceReconstruction(self, org, seqs):

        # if either of these two is empty, another must be empty.
        if not org:
            return not seqs
        if not seqs:
            return not org
        # for corner case like: org = [1], seq = [[1,1]] or seq = [[1], [1], [1]]
        # or seq = [[1], [1], [2]]
        if len(org) == 1:
            for seq in seqs:
                if seq != org: return False
            return True

        nodes = set(org)
        edges = collections.defaultdict(set)
        for seq in seqs:
            # seq could be []
            if not seq: continue
            # a disconnected node that won't be added to edges but we need to check it
            if seq[0] not in nodes: return False
            n = len(seq)
            # if len(seq) == 1, this for loop won't be excuted
            for i in xrange(n - 1):
                edges[seq[i]].add(seq[i + 1])

        print edges

        # won't cover the case when len(org) == 1.
        for i in xrange(len(org) - 1):
            node, next = org[i], org[i + 1]
            if node not in edges or next not in edges[node]:
                return False
            del edges[node]
            print edges

        # for case like org = [1,2,3,4], seqs = [[1,2,3], [2,3], [3,4], [4,3]],
        # the edges could still not be empty in the end, so we need to check it
        # instead of directly returning True
        return not edges



org = [1, 2, 3]
seq = [[1,2], [1,3]]
Sol = Solution()
print Sol.sequenceReconstruction(org, seq)

