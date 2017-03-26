
'''
Binary search to reduce the time complexity to o(log(n)), the idea about deciding
the next search area comes from leetcode274: H-Index.
'''

class Solution(object):
    def hIndex(self, citations):

        start, end = 0, len(citations)-1
        n = len(citations)
        hIndex = 0
        while start <= end:
            mid = (start + end)/2
            if n- mid <= citations[mid]:
                hIndex = n - mid
                end = mid-1
            else:
                start = mid+1

        return hIndex