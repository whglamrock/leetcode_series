
from collections import defaultdict, deque

# classic toposort solution O(m * n) solution where n is the avg length of word
# if not for detecting circle, soly using one of greater/less can do the toposort

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ''
        if len(words) == 1:
            return words[0]

        # build the less & greater relationship.
        less, greater = self.buildRelationship(words)

        # using q to conduct the topology sort.
        charSet = set(''.join(words))
        q = deque()
        for char in charSet:
            # using the greater relationship to build the toposort queue but
            # we use less to perform the toposort to detect invalid case
            if char not in greater:
                q.append(char)

        ans = []
        # pop the verticles that don't have "children" first
        while q:
            char = q.popleft()
            ans.append(char)
            if char not in less:
                continue
            for greaterChar in less[char]:
                greater[greaterChar].discard(char)
                if not greater[greaterChar]:
                    del greater[greaterChar]
                    q.append(greaterChar)

        return ''.join(ans) if not greater else ''

    # return a less list & greater list to build the relationship
    def buildRelationship(self, words):
        less, greater = defaultdict(set), defaultdict(set)
        for i in xrange(len(words) - 1):
            minLen = min(len(words[i]), len(words[i + 1]))
            for j in xrange(minLen):
                if words[i][j] == words[i + 1][j]:
                    continue
                less[words[i][j]].add(words[i + 1][j])
                greater[words[i + 1][j]].add(words[i][j])
                break

        return less, greater



words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
print Solution().alienOrder(words)