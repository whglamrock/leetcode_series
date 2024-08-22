
# Intuition: we need to be able to think of greedy algorithm instead of DP to get to the optimal time complexity.
# 1) We always wanna use source to match as many chars in target's prefix as possible -> this will yield best result.
# proof:
#   a) assume we used k source subsequences to match target[:x] and target[:y] and x < y;
#   b) this means len(target[x:]) > len(target[y:]) and target[x:] & target[y:] share a suffix.
#   c) there is no way target[x:] would require fewer number of source subsequences to match than target[y:]
#   d) since target[:x] and target[:y] both used k source subsequences, this means the x approach is guaranteed to have
#      same or worse result than the y approach.
# 2) In worst case O(M * N) solution. e.g., source = 'abdcefg', target = 'ggggggg'
class Solution(object):
    def shortestWay(self, source: str, target: str) -> int:
        sourceSet = set(source)
        i, j = 0, 0
        m, n = len(source), len(target)

        count = 0
        while j < n:
            # this condition decides that we need to return count + 1, not count
            if i == m:
                count += 1
                i = 0

            while i < m and j < n and source[i] == target[j]:
                i += 1
                j += 1

            if j < n and target[j] not in sourceSet:
                return -1

            while i < m and j < n and source[i] != target[j]:
                i += 1

        return count + 1


print(Solution().shortestWay("abc", "abcbc"))
print(Solution().shortestWay("abc", "acdbc"))
print(Solution().shortestWay("xyz", "xzyxz"))
