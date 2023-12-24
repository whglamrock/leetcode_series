from functools import lru_cache


# time complexity is exponential in worse case (could be 3^n: if string has a lot of 3 digit substrings,
# number of recursions is O(n)). Using cache can improve speed
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        return self.backtrackingSearch(0, 0, s1, s2, 0)

    # the s1/s2's length is after compression. The original length of the string can be super long
    def possibleLengths(self, s: str) -> list:
        possibleLens = [int(s)]
        if len(s) == 2:
            possibleLens.append(int(s[0]) + int(s[1]))
        elif len(s) == 3:
            possibleLens.append(int(s[0]) + int(s[1]) + int(s[2]))
            possibleLens.append(int(s[0]) + int(s[1:]))
            possibleLens.append(int(s[:2]) + int(s[2]))

        return possibleLens

    # backtracking search
    # diff < 0 means we are lagging behind in advancing rightward in s2
    # diff > 0 means we are lagging behind in advancing rightward in s1
    @lru_cache(maxsize=None, typed=False)
    def backtrackingSearch(self, i: int, j: int, s1: str, s2: str, diff: int) -> bool:
        if i == len(s1) and j == len(s2):
            return diff == 0
        if i < len(s1) and s1[i].isdigit():
            ii = i
            while ii < len(s1) and s1[ii].isdigit():
                ii += 1
            # if we finish scanning the s1[i:ii] as digits, it means
            # s2 "owes" possibleLen number of characters
            for possibleLen in self.possibleLengths(s1[i:ii]):
                if self.backtrackingSearch(ii, j, s1, s2, diff - possibleLen):
                    return True
        elif j < len(s2) and s2[j].isdigit():
            jj = j
            while jj < len(s2) and s2[jj].isdigit():
                jj += 1
            for possibleLen in self.possibleLengths(s2[j:jj]):
                if self.backtrackingSearch(i, jj, s1, s2, diff + possibleLen):
                    return True
        elif diff == 0:
            if i == len(s1) or j == len(s2) or s1[i] != s2[j]:
                return False
            return self.backtrackingSearch(i + 1, j + 1, s1, s2, 0)
        elif diff < 0:
            if j == len(s2):
                return False
            # because s2 "owes" characters, so we advance in s2
            return self.backtrackingSearch(i, j + 1, s1, s2, diff + 1)
        else:
            if i == len(s1):
                return False
            # because s1 "owes" characters, so we advance in s1
            return self.backtrackingSearch(i + 1, j, s1, s2, diff - 1)


print(Solution().possiblyEquals(s1="internationalization", s2="i18n"))
print(Solution().possiblyEquals(s1="l123e", s2="44"))
print(Solution().possiblyEquals(s1="a5b", s2="c5b"))
