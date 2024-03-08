class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        m, n = len(word), len(abbr)
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                # shouldn't have leading 0
                if abbr[j] == '0':
                    return False
                curr = int(abbr[j])
                while j + 1 < n and abbr[j + 1].isdigit():
                    curr = curr * 10 + int(abbr[j + 1])
                    j += 1
                i += curr
                j += 1
            else:
                return False

        return i == m and j == n


print(Solution().validWordAbbreviation("internationalization", "i12iz4n"))
