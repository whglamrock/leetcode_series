from collections import Counter, defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        charCount = Counter(s)
        countToChars = defaultdict(set)
        minCount, maxCount = 2147483647, 0
        for char, count in charCount.items():
            countToChars[count].add(char)
            minCount = min(minCount, count)
            maxCount = max(maxCount, count)

        ans = []
        for count in range(maxCount, minCount - 1, -1):
            if count not in countToChars:
                continue
            for char in countToChars[count]:
                for i in range(count):
                    ans.append(char)

        return ''.join(ans)
