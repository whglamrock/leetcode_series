
# O(N) counting sort solution

class Solution(object):
    def hIndex(self, citations):

        if not citations:
            return 0

        n = len(citations)
        # since the citation of each paper could be 0 to n, its length has to be n + 1
        counting = [0] * (n + 1)

        for i, cite in enumerate(citations):
            if cite > n:
                counting[n] += 1
            else:
                counting[cite] += 1

        currsum = 0
        for i in xrange(n, -1, -1):
            # the currsum counts how many papers in total have at least i citations
            currsum += counting[i]
            if currsum >= i:
                return i

        return 0



Sol = Solution()
citations = [3, 0, 6, 1, 5]
print Sol.hIndex(citations)



'''
# simple guaranteed O(NlogN) sorting solution:

class Solution(object):
    def hIndex(self, citations):

        # (n - i) <= citations[i]
        #   (n - i) articles have at least citations[i] citations
        #   i increases, n - i decreases
        citations.sort()
        n = len(citations)

        for i in xrange(n):
            if n - i <= citations[i]:
                return n - i

        return 0
'''




