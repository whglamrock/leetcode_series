
class Solution(object):
    def wordBreak(self, s, wordDict):

        # the dfs returns all possible combination of s
        def dfs(s, wordDict, dic):
            # to avoid TLE. Because multiple feasible combinations of words can fors s.
            # e.g., is 's' = 'abc' is the prefix of s = 'abcdef',
            # wordDict = {'a', 'b', 'c', 'ab', 'bc', 'abc', 'def'}, the 's' = 'abc' has many ways to
            # be formed, then we don;t need to the below for loop too many times.
            if s in dic:
                return dic[s]

            res = []
            # the bottom case of dfs, when recursion goes after the last char of s
            if len(s) == 0:
                res.append(s)
                return res

            for word in wordDict:
                if s.startswith(word):
                    # the sublist stores all possible combinations of s[len(word):]
                    # e.g., if s[len(word):] == 'abcbc', wordDict = {'ab', 'abc', 'cbc', 'bc'}
                    # then the sublist = ['ab cbc', 'abc bc']
                    sublist = dfs(s[len(word):], wordDict, dic)
                    # there is only one possible case when a sub equals to '':
                    # that is when sublist = ['']
                    for sub in sublist:
                        if sub:
                            res.append(word + ' ' + sub)
                        else:
                            res.append(word)

            # the res stores all possible combinations of s;
            # the dic doesn't contain key ''.
            # the dic is filled from s's back to s's head (the key in dic is s's suffix)
            dic[s] = res
            return res

        return dfs(s, wordDict, {})



# try print word, sublist, dic in every for loop to see the execution
Sol = Solution()
s = "catsanddog"
wordDict = {"cat","cats","and","sand","dog", "an", "ddog"}
print Sol.wordBreak(s, wordDict)
