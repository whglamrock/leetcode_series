from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charCount = Counter(s)
        ans = []
        for char in order:
            if char not in charCount:
                continue
            for i in range(charCount[char]):
                ans.append(char)
            del charCount[char]

        # deal with leftover chars (the ones with no order restriction)
        for char in charCount:
            for i in range(charCount[char]):
                ans.append(char)

        return ''.join(ans)


print(Solution().customSortString("cba", "abcd"))
