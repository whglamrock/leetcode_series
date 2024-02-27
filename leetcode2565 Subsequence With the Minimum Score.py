# The hardest part is to think of dividing s into 2 parts and use each of them of match t's prefix and suffix:
# a) We have to realize that t is most likely not subsequence of s (if t indeed is a subsequence of s, return 0);
# b) Until you use two pointers to scan through both s & t, there is NO WAY to know what the first/last index is
# to remove from t; i.e., the state of "first" or "last" is ONLY valid for certain prefix/suffix of s you scanned so far
# c) We really don't give a shit if any chars in between "first" & "last" removed index of t can together become
# a subsequence of s. We really don't care. We can just remove all of them.
# d) Based on above, you might be able to think of this idea: scanning through the whole s, find the longest prefix/suffix
# of t it can match and find both lengths; then use len(t) - prefix - suffix. This idea is not correct because there
# may be overlapping between the substrings of s you use to match t's prefix/suffix.

# That's how we can come to the full algorithm (you can also see: https://www.youtube.com/watch?v=eVAeTG5VjVM&ab_channel=CodeWithU-DAY)
# 1) For index i of s, try to use s[:i] to match the longest prefix of t, and use s[i:] to match the longest suffix of t
# 2) The reason we are doing above is (if we decide to use s[:i] and s[i:] to match t's prefix and suffix, respectively):
# 2.1) the first char in t's prefix that doesn't match s[:i] will need to be removed;
# 2.2) the first char (from right to left) in t's suffix that doesn't match s[i:] will also need to be removed
# 3) We should be able to observe that we can remove all indexes of t in between 2.1) and 2.2) and it won't affect the result
# 4) We calculate the index of such first char in prefix/suffix of t for all s[i] and calculate the length of the window
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        suffix = [-1] * n
        j = 0
        for i in range(n - 1, -1, -1):
            if j < m and s[i] == t[m - 1 - j]:
                j += 1
            suffix[i] = j

        j = 0
        prefix = [-1] * n
        for i in range(n):
            if j < m and s[i] == t[j]:
                j += 1
            prefix[i] = j

        ans = len(t)
        for i in range(1, n):
            # if ans becomes < 0 it means t is a already subsequence of s and we don't need to remove any index
            ans = min(ans, m - prefix[i - 1] - suffix[i])
        # first part of s to match t's prefix is empty
        ans = min(ans, m - suffix[0])
        # second part of s to match t's suffix is empty
        ans = min(ans, m - prefix[n - 1])

        return max(ans, 0)
