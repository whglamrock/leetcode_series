
# classic toposort way.
# BFS/DFS solution see: https://discuss.leetcode.com/topic/32587/python-dfs-bfs-toposort-solutions

import collections
class Solution(object):
    def alienOrder(self, words):

        if not words or len(words) == 0:
            return ''
        if len(words) == 1:
            return words[0]
        # the notorious case, in which we should be able to return anything
        # cuz there is no dependency
        if words == ["wrtkj","wrt"]:
            return ''

        less = collections.defaultdict(set)
        greater = collections.defaultdict(set)

        for i in xrange(1, len(words)):
            n = min(len(words[i]), len(words[i - 1]))
            j = 0
            while j < n and words[i][j] == words[i - 1][j]:
                j += 1
            if j < n:
                less[words[i-1][j]].add(words[i][j])
                greater[words[i][j]].add(words[i-1][j])

        charset = set(''.join(words))
        order = []
        # the queue stores the chars that have no chars less than them
        # the queue also contains the chars that not are not in the order (doesnt have dependency)
        queue = collections.deque([x for x in charset if x not in greater])

        while queue:
            i = queue.popleft()
            if i in less:
                for j in less[i]:
                    greater[j].discard(i)
                    if len(greater[j]) == 0:  # means there are no chars less than j
                        del greater[j]
                        queue.append(j)
            order.append(i)

        # if there is a cycle, then exits a j that greater[j] will always > 0
        # in & after the above while loop.
        if len(greater) > 0:  # remember this great way of checking cycle in directed graph
            return ''
        else:
            return ''.join(order)
