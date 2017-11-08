
class Solution(object):
    def letterCombinations(self, digits):

        if not digits: return []

        mapping = {'1': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        ans = ['']
        for digit in digits:
            new = []
            for combi in ans:
                for letter in mapping[digit]:
                    new.append(combi + letter)
            if new: ans = new

        return ans



digits = '237'
Sol = Solution()
print Sol.letterCombinations(digits)













