from heapq import *

# we add char one at a time instead of trying to add 2 same chars at once. Otherwise it's hard to deal with some
# edge cases like "aabaacaabaaca" (a = 9, b = 2, c = 2)
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a != 0:
            heappush(pq, [-a, 'a'])
        if b != 0:
            heappush(pq, [-b, 'b'])
        if c != 0:
            heappush(pq, [-c, 'c'])

        ans = []
        while pq:
            count, char = heappop(pq)
            if len(ans) >= 2 and ans[-1] == ans[-2] == char:
                if not pq:
                    break
                secondMostCount, secondMostChar = heappop(pq)
                ans.append(secondMostChar)
                secondMostCount += 1
                if secondMostCount:
                    heappush(pq, [secondMostCount, secondMostChar])
                heappush(pq, [count, char])
                continue

            # regular case
            ans.append(char)
            count += 1
            if count:
                heappush(pq, [count, char])

        return ''.join(ans)
