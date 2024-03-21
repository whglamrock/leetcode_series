class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i, j = 0, 0
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                curr = 0
                while j < n and abbr[j].isdigit():
                    curr = curr * 10 + int(abbr[j])
                    j += 1
                i += curr
            else:
                return False

        return i == m and j == n


print(Solution().validWordAbbreviation("internationalization", "i12iz4n"))
