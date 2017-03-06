
class Solution(object):
    def letterCombinations(self, digits):

        if not digits: return []

        ans = []
        pool = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def helper(s, path):
            if not s:
                ans.append(path)
                return
            for letter in pool[int(s[0])]:
                helper(s[1:], path + letter)

        helper(digits, '')
        return ans



digits = '237'
Sol = Solution()
print Sol.letterCombinations(digits)













