
# the key is to use a dic to store visited patterns
# further optimization could be done using a backward dic to avoid 'string[:i] not in dic.values()'

class Solution(object):
    def wordPatternMatch(self, pattern, str):

        return self.dfs({}, pattern, str)

    def dfs(self, dic, pattern, string):

        if len(pattern) == 0 and len(string) > 0:
            return False
        if len(pattern) == 0 and len(string) == 0:
            return True

        # because i needs to be like [:i], so biggest i can be len(string) - len(pattern) + 1
        for i in xrange(1, len(string) - len(pattern) + 2):

            # means this char in pattern is a new letter, and corresponding substring can't
            # match other stores substrings
            if pattern[0] not in dic and string[:i] not in dic.values():
                dic[pattern[0]] = string[:i]
                if self.dfs(dic, pattern[1:], string[i:]):
                    return True
                if pattern[0] in dic: del dic[pattern[0]]

            # this char has already existed in dic, so the corresponding substring has to match
            elif pattern[0] in dic and string[:i] == dic[pattern[0]]:
                if self.dfs(dic, pattern[1:], string[i:]):
                    return True

        return False