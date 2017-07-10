
# idea: definitely binary search 'cause the citations is sorted
# the ideal condition of search is to find a citation[i] that citation[i] == n - i
# remember the definition of h-index: all citation[i:] >= n - i, citations[:i] <= n - 1, where
#   both comparison symbol contain "=="

class Solution(object):
    def hIndex(self, citations):

        if not citations:
            return 0

        n = len(citations)
        # P.S.: when using "while l < r" instead of "<=", the mid won't be out of range
        l, r = 0, n

        # exit condition: l == r
        while l < r:
            mid = l + (r - l) / 2
            if citations[mid] == n - mid:
                return n - mid
            # in this case, the n - mid is still candidate
            elif citations[mid] > n - mid:
                r = mid
            # all citations[:mid + 1] are < n - mid
            else:
                l = mid + 1

        # it also applies to when n - l == 0
        return n - l



'''
class Solution(object):
    def hIndex(self, citations):

        if not citations:
            return 0

        n = len(citations)
        # when using "while l < r" instead of "<=", the mid won't be out of range
        l, r = 0, n - 1  # P.S., r is not initiated as n anymore!   

        if l == r:  # e.g., citation = [0]
            return 1 if citations[0] >= 1 else 0

        # exit condition: l == r
        while l < r:
            mid = l + (r - l) / 2
            if citations[mid] == n - mid:
                return n - mid
            # in this case, the n - mid is still candidate
            elif citations[mid] > n - mid:
                r = mid
            # all citations[:mid + 1] are < n - mid
            else:
                l = mid + 1

        if l == 0:
            return n if citations[0] >= n else 0
        else:   # for case like [0, 0] and [0, 0, 0], etc.
            # the second comparison symbol has to be "<=" (e.g. when citations = [1, 1])
            return n - l if (citations[l] >= n - l and citations[l - 1] <= n - l) else 0
'''