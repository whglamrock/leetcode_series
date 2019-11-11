
# The idea is to use 2 two dicts to store visited patterns

class Solution(object):
    def wordPatternMatch(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.dfs(pattern, string, {}, {})

    def dfs(self, pattern, string, patternToString, stringToPattern):
        if len(pattern) == 0 and len(string) > 0:
            return False
        if len(pattern) == 0 and len(string) == 0:
            return True

        # for the next recursion, the len(string[i:]) >= len(pattern[1:]);
            # so when len(string[i:]) == len(pattern) - 1 => len(string) - i == len(pattern) - 1
            # => i = len(string) - len(pattern) + 1 and this is the biggest i
        for i in xrange(1, len(string) - len(pattern) + 2):
            subString = string[:i]
            if pattern[0] not in patternToString and subString not in stringToPattern:
                patternToString[pattern[0]] = subString
                stringToPattern[subString] = pattern[0]
                if self.dfs(pattern[1:], string[i:], patternToString, stringToPattern):
                    return True
                del patternToString[pattern[0]]
                del stringToPattern[subString]
            elif pattern[0] in patternToString and patternToString[pattern[0]] == subString:
                if self.dfs(pattern[1:], string[i:], patternToString, stringToPattern):
                    return True

        return False



print Solution().wordPatternMatch("abab", "redblueredblue")
print Solution().wordPatternMatch("aaaa", "asdasdasdasd")
print Solution().wordPatternMatch("aabb", "xyzabcxzyabc")