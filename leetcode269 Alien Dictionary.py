
from collections import defaultdict, deque

# classic toposort way.
# BFS/DFS solution see: https://discuss.leetcode.com/topic/32587/python-dfs-bfs-toposort-solutions

class Solution(object):
    def alienOrder(self, words):

        if not words:
            return ''
        if len(words) == 1:
            return words[0]

        smaller, bigger = defaultdict(set), defaultdict(set)
        for i in xrange(1, len(words)):
            j, n = 0, min(len(words[i - 1]), len(words[i]))
            while j < n and words[i - 1][j] == words[i][j]:
                j += 1
            if j < n:
                smaller[words[i - 1][j]].add(words[i][j])
                bigger[words[i][j]].add(words[i - 1][j])

        letters = set(''.join(words))
        q = deque()
        for letter in letters:
            if letter not in bigger:
                q.append(letter)

        ans = []
        while q:
            letter = q.popleft()
            ans.append(letter)
            if letter in smaller:
                for biggerletter in smaller[letter]:
                    bigger[biggerletter].discard(letter)
                    if len(bigger[biggerletter]) == 0:
                        # append it to q, not ans because the q could also be in bigger
                            # it's like "putting the vertex without children in the unvisited set and
                            # look up its parents"
                        q.append(biggerletter)
                        del bigger[biggerletter]

        return ''.join(ans) if len(bigger) == 0 else ''



words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
print Solution().alienOrder(words)