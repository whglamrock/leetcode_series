
'''
The worst case is o(n^2) when: 1) the citations array is in descending order, and within every
while loop of the hIndex function, the n-current > citations[current] (this is under extreme circumstances
cuz when current is very big, n-current will be small; And since all elements on the left of
citations[current] are smaller than it, the citations[current] will be big); 2) Similarly, the citations
array is in ascending order, and within every while loop of the hIndex function, the n-current <=
citations[current].
On average, its o(n) time complexity, see: https://leetcode.com/discuss/60349/better-solution-than-hint-no-extra-space
'''

class Solution(object):
    def dividedByPartition(self, a, start, end):

        if start == end:
            return end

        p = a[end]
        head = start
        for current in xrange(start, end):
            if a[current]<p:        # swap a[current], a[head] but the index of current/head remains.
                a[current], a[head] = a[head], a[current]       # every element smaller/bigger than p will be
                head += 1                                       # moved to the left/right of a[head]

        a[end] = a[head]        # since the 'pivot' is a[end], it needs to be swapped with a[head]
        a[head] = p         # thus every element on the left/right of a[head] will be smaller/bigger than it.
        return head

    def hIndex(self, citations):

        n = len(citations)
        start, end = 0, n-1
        hIndex = 0

        while start <= end:
            current = self.dividedByPartition(citations, start, end)    # another 'current', means differently
            if n - current <= citations[current]:
                hIndex = n - current
                end = current - 1           # search the left side current to see if there exits bigger n-current
            else:           # n-current > citations[current]
                start = current + 1
                # move the search to the right side so current will increase
                # current can't decrease cuz if so, n-current will increase. And since we've proved
                # all elements on the left of citations[current] is smaller than it, the citation[current]
                # will decrease if we search the left side, then the n-current <= citations[current] will
                # never happen. Therefore, the start = current+1, search moves to the right side.

        return hIndex



Sol = Solution()
citations = [3, 0, 6, 1, 5]
print Sol.hIndex(citations)




