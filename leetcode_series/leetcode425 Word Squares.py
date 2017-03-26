
# the idea is to use hashtable to act as prefix tree.

import collections

class Solution(object):
    def wordSquares(self, words):

        dic = collections.defaultdict(list)
        n = len(words[0])
        for word in words:
            for i in xrange(n):
                dic[word[:i + 1]].append(word)  # very important idea!

        ans = []
        def helper(lst):
            if len(lst) == n:
                ans.append(lst)
                return
            m = len(lst)
            prefix = ''
            for i in xrange(m):
                prefix += lst[i][m]
            if prefix in dic:
                for word in dic[prefix]:
                    helper(lst + [word])

        for word in words:
            helper([word])
        return ans