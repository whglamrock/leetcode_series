# the thought is pretty much like DFS
# the Hashmap dic stores the steps can be taken from each stone (key is stone, value is a set)

class Solution(object):
    def canCross(self, stones):

        if not stones or len(stones) < 1 or stones[1] != 1:
            return False

        dic = {}
        for stone in stones:
            dic[stone] = set()
        dic[0].add(1)

        for i in xrange(len(stones) - 1):
            stone = stones[i]
            for step in dic[stone]:
                reach = step + stone
                if reach not in dic:
                    continue
                if reach == stones[-1]:
                    return True
                dic[reach].add(step)
                dic[reach].add(step + 1)
                if step - 1 > 0:
                    dic[reach].add(step - 1)

        return False



Sol = Solution()
stones = [0, 1, 2, 4, 5, 6, 7, 9, 10, 11, 13]
print Sol.canCross(stones)



'''
# DFS solution

class Solution(object):
    def canCross(self, stones):

        if not stones or len(stones) < 1 or stones[1] != 1: return False

        self.stoneset = set(stones)
        self.destination = stones[-1]
        # store dead ends; each dead end is with a specific currstone and laststep
        self.check = set()

        return self.helper(1, 1)

    def helper(self, laststep, currstone):

        # memo check
        if (currstone, laststep) in self.check:
            return False

        # corner case check
        if currstone not in self.stoneset or currstone == 0:
            return False

        if currstone == self.destination:
            return True

        candidates = [laststep, laststep + 1]
        if laststep - 1 > 0:
            candidates.append(laststep - 1)
        for candidate in candidates:
            if candidate + currstone in self.stoneset:
                if self.helper(candidate, currstone + candidate):
                    return True

        self.check.add((currstone, laststep))
        return False
'''