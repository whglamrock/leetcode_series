from collections import Counter

# greedy algo: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/solutions/927549/c-java-python-3-greedy/
# if there is count conflict, decrease the count of this char until there is no conflict
class Solution:
    def minDeletions(self, s: str) -> int:
        charCount = Counter(s)
        ans = 0
        usedCounts = set()

        for char, count in charCount.items():
            while count > 0 and count in usedCounts:
                count -= 1
                ans += 1
            if count > 0:
                usedCounts.add(count)

        return ans


print(Solution().minDeletions("aaaaabbbcc"))
print(Solution().minDeletions("aaabbbcc"))
print(Solution().minDeletions("ceabaacb"))



