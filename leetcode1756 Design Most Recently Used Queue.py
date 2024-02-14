# Naive O(n) solution. In interview it should be ok because the O(log(N)) solution really has to:
# 1) Either use non python built-in library to make it work like SortedDict (shown at the bottom);
# 2) Or use some extremely unpopular algorithm like sqrt decomposition: https://leetcode.com/problems/design-most-recently-used-queue/solutions/1065076/java-sqrt-decomposition-short-doubly-linked-list/
# In real interview we just need to mention the O(log(N)) idea using the SortedDict
class MRUQueue:
    def __init__(self, n: int):
        self.queue = [i + 1 for i in range(n)]

    def fetch(self, k: int) -> int:
        k -= 1
        val = self.queue[k]
        del self.queue[k]
        self.queue.append(val)
        return val


mrq = MRUQueue(8)
print(mrq.fetch(3))
print(mrq.fetch(5))
print(mrq.fetch(2))
print(mrq.fetch(8))


'''
from sortedcontainers import SortedDict

class MRUQueue:
    def __init__(self, n: int):
        self.rankToNum = SortedDict()
        self.rank = 0
        for i in range(1, n + 1):
            self.rankToNum[self.rank] = i
            self.rank += 1

    def fetch(self, k: int) -> int:
        key, value = self.rankToNum.popitem(k - 1)
        self.rank += 1
        self.rankToNum[self.rank] = value
        return value
'''
