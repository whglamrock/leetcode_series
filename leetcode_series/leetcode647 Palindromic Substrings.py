
from collections import defaultdict

class Solution(object):
    def countSubstrings(self, s):

        if not s:
            return 0

        length_to_indices = defaultdict(set)
        n = len(s)
        for i in xrange(n):
            length_to_indices[1].add((i, i))
            if i < n - 1 and s[i] == s[i + 1]:
                length_to_indices[2].add((i, i + 1))

        curr_len = 3
        # curr_len can == n. Also, only extend the list by 2 chars
        while curr_len <= n:
            for l, r in length_to_indices[curr_len - 2]:
                if l - 1 >= 0 and r + 1 < n and s[l - 1] == s[r + 1]:
                    length_to_indices[curr_len].add((l - 1, r + 1))
            curr_len += 1

        ans = 0
        for indices_list in length_to_indices.values():
            ans += len(indices_list)

        return ans
