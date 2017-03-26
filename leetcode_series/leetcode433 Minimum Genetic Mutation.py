
# this question is ranked medium because the length of gene is 8,
# and memory and time limit is not very restrict.

class Solution(object):
    def minMutation(self, start, end, bank):

        if start == end: return 1
        if (not bank) or (end not in bank): return -1

        bankset = {start, end}
        for gene in bank:
            bankset.add(gene)

        # check if two genes are one step away.
        def compare(a, b):
            count = 0
            for i in xrange(8):
                if a[i] != b[i]: count += 1
            if count != 1:
                return False
            return True

        bankdic = {}
        # graph construction. O(N^2) time.
        for gene in bankset:
            bankdic[gene] = set()
            for othergene in bankset:
                if gene != othergene and compare(gene, othergene):
                    bankdic[gene].add(othergene)
            if len(bankdic[gene]) == 0:
                del bankdic[gene]

        self.ans = -1
        def findpath(graph, b, last, path):
            if b in graph[last]:
                if self.ans == -1:
                    self.ans = len(path)
                else:
                    self.ans = min(len(path), self.ans)
                return
            next = []
            for i in graph[last]:
                if i not in path:
                    next.append(i)
            if not next: return      # the path ends, no valid next hop
            for i in next:
                findpath(graph, b, i, path | {i})
            return

        findpath(bankdic, end, start, {start})
        return self.ans
