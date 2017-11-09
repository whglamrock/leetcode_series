
# BFS solution

class Solution(object):
    def numSquares(self, n):

        if n < 4:
            return n

        pool = []
        i = 1
        while i * i <= n:
            pool.append(i * i)
            i += 1

        todo = {n}
        cnt = 0
        while todo:
            cnt += 1
            next = set()
            for x in todo:    # we don't need to track which numbers we used, but instead how many numbers.
                for y in pool:
                    if x == y:
                        return cnt
                    elif x < y:
                        break
                    next.add(x - y)    # avoid duplicates
            todo = next

        return cnt

