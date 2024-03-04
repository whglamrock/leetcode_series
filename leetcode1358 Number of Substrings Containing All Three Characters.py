from collections import defaultdict

# count the number of substrings that ends at each s[i], the rightmost of startIndex j of s[j:i + 1] should be
# the min of right most indexes of a/b/c. Then all start index (j) in range [0, rightmostStartIndex] suffice.
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        letterToIndexes = defaultdict(list)
        ans = 0
        for i, char in enumerate(s):
            if char in 'abc':
                letterToIndexes[char].append(i)
            if len(letterToIndexes) == 3:
                minOfLatestAbcIndex = min(letterToIndexes['a'][-1], letterToIndexes['b'][-1], letterToIndexes['c'][-1])
                ans += minOfLatestAbcIndex + 1

        return ans
