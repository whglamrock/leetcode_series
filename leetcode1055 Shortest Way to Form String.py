
# in worst case O(M * N) solution. e.g., source = 'abdcefg', target = 'ggggggg'
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
