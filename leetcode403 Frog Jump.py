
# DFS & memoization solution

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # stones list will have at least 2 stones
        if stones[1] != 1:
            return False

        return self.dfs(stones[1], 1, stones[-1], set(stones), set())

    def dfs(self, currStone, lastStep, destination, stonesSet, memo):

        if (currStone, lastStep) in memo:
            return False
        if currStone not in stonesSet or currStone == 0:
            return False

        if currStone == destination:
            return True

        steps = [lastStep, lastStep + 1]
        if lastStep - 1 > 0:
            steps.append(lastStep - 1)

        for step in steps:
            if self.dfs(currStone + step, step, destination, stonesSet, memo):
                return True

        memo.add((currStone, lastStep))
        return False



print Solution().canCross([0, 1, 2, 4, 5, 6, 7, 9, 10, 11, 13])
print Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11])



'''
# an interesting hashmap solution. A little bit slower than DFS + Memo solution

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
'''