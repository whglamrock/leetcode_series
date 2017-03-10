# not very efficient but 0(N) time solution. The max number of elements in heap is 26,
# so the heap operations will all take constant time.
from heapq import *
class Solution(object):
    def rearrangeString(self, string, k):

        dic = {}
        for char in string:
            if char not in dic:
                dic[char] = -1
            else:
                dic[char] -= 1

        heap = []
        for item in dic:
            heap.append((dic[item], item))
        heapify(heap)

        res = []
        while len(res) < len(string):
            if not heap:
                return ''
            freq, char = heappop(heap)
            stack = []
            res.append(char)
            for i in xrange(k - 1):
                if len(string) == len(res):
                    return ''.join(res)
                if not heap:    # string = "aaabc", k = 3 belongs to this cas
                    return ''
                fre, nex = heappop(heap)
                res.append(nex)
                if fre < -1:  # means this char is still available after this round
                    stack.append((fre + 1, nex))
            while stack:
                heappush(heap, stack.pop())
            if freq < -1:
                heappush(heap, (freq + 1, char))

        return ''.join(res)